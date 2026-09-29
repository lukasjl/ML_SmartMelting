function run_smartweld_matlab()
%RUN_SMARTWELD_MATLAB Start the original SmartWeld MATLAB application.
% Does not invent undocumented solver arguments.

mfiles = fullfile(getenv('USERPROFILE'), 'SmartWeld', 'Mfiles');
if ~isfolder(mfiles)
    error('SmartWeld M-files not found. Run bootstrap_smartweld.ps1 first.');
end

addpath(genpath(mfiles));
mainFile = fullfile(mfiles, 'Main.m');
if ~isfile(mainFile)
    error('Main.m not found under %s', mfiles);
end

fprintf('Starting original SmartWeld Main.m from %s\n', mfiles);
run(mainFile);
end
