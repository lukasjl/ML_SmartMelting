function smartweld_batch_entry()
%SMARTWELD_BATCH_ENTRY Execute the recovered OSLW model without the GUI.
%
% Verified source path:
%   app_specific_data -> schedulermodels -> queryfunc
%
% Inputs are supplied by smartweld_backend.ps1 through environment variables.
% OSLW source uses power [W], travel speed [mm/s], and spot diameter [cm].

global guiGlobals;
global currentApplication;

infile = getenv('SMARTWELD_INPUT_JSON');
outfile = getenv('SMARTWELD_OUTPUT_JSON');
if isempty(infile) || isempty(outfile)
    error('SMARTWELD_INPUT_JSON and SMARTWELD_OUTPUT_JSON are required.');
end

power_W = str2double(getenv('SMARTWELD_POWER_W'));
speed_mm_s = str2double(getenv('SMARTWELD_TRAVEL_SPEED_MM_S'));
spot_cm = str2double(getenv('SMARTWELD_SPOT_DIAMETER_CM'));
material = strtrim(getenv('SMARTWELD_MATERIAL'));
gas = lower(strtrim(getenv('SMARTWELD_SHIELDING_GAS')));

if any(isnan([power_W speed_mm_s spot_cm]))
    error('Power, travel speed and spot diameter must be numeric.');
end

currentApplication = 'OSLW';
guiGlobals = struct();
app_specific_data;

guiGlobals.mat_index = 0;
for k = 1:size(guiGlobals.material_label,1)
    label = strtrim(guiGlobals.material_label(k,:));
    if strcmpi(label, material) || (length(material) >= 3 && length(label) >= 3 && ...
            strcmpi(label(1:3), material(1:3)))
        guiGlobals.mat_index = k;
        break;
    end
end
if guiGlobals.mat_index == 0
    error('SmartWeld OSLW material not found: %s', material);
end

if strcmp(gas,'argon')
    guiGlobals.gas_index = 1;
elseif strcmp(gas,'helium')
    guiGlobals.gas_index = 2;
else
    error('SmartWeld OSLW shielding gas must be argon or helium: %s', gas);
end

spot_index = find(abs(guiGlobals.spot_diameters - spot_cm) < 1e-12, 1);
if isempty(spot_index)
    error('Spot diameter %.12g cm is not one of the verified OSLW lens spot diameters.', spot_cm);
end
guiGlobals.spot_index = spot_index;

outputs = queryfunc([power_W speed_mm_s spot_cm]);
write_result(outfile, power_W, speed_mm_s, spot_cm, material, gas, outputs);
fprintf('SmartWeld OSLW completed: P=%.12g W, V=%.12g mm/s, D=%.12g cm\n', ...
        power_W, speed_mm_s, spot_cm);
end

function write_result(path, power_W, speed_mm_s, spot_cm, material, gas, outputs)
fid = fopen(path, 'w');
if fid < 0
    error('Cannot create SmartWeld output: %s', path);
end
c = onCleanup(@() fclose(fid)); %#ok<NASGU>

fprintf(fid, '{\n');
fprintf(fid, '  "status": "completed",\n');
fprintf(fid, '  "model_id": "OSLW",\n');
fprintf(fid, '  "smartweld_version": "3.0",\n');
fprintf(fid, '  "inputs": {"power_W": %.15g, "travel_speed_mm_s": %.15g, "spot_diameter_cm": %.15g, "material": "%s", "shielding_gas": "%s"},\n', ...
        power_W, speed_mm_s, spot_cm, json_escape(material), json_escape(gas));
fprintf(fid, '  "outputs": {"energy_transfer_efficiency": %.15g, "melting_efficiency": %.15g, "weld_width_mm": %.15g, "penetration_depth_mm": %.15g, "penetration_sensitivity_per_W": %.15g},\n', ...
        outputs(1), outputs(2), outputs(3), outputs(4), outputs(5));
fprintf(fid, '  "units": {"power_W": "W", "travel_speed_mm_s": "mm/s", "spot_diameter_cm": "cm", "weld_width_mm": "mm", "penetration_depth_mm": "mm", "penetration_sensitivity_per_W": "mm/W"}\n');
fprintf(fid, '}\n');
end

function s = json_escape(s)
s = strrep(s, '\', '\\');
s = strrep(s, '"', '\"');
end
