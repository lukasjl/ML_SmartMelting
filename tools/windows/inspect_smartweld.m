function inspect_smartweld()
%INSPECT_SMARTWELD Inventory original SmartWeld MATLAB sources.
% Compatible with legacy MATLAB releases; does not execute solver models.

root = fullfile(getenv('USERPROFILE'), 'SmartWeld', 'Mfiles');
if exist(root, 'dir') ~= 7
    error('SmartWeld M-files directory not found: %s', root);
end

files = local_list_m(root);
out = fullfile(root, 'smartweld_source_inventory.txt');
fid = fopen(out, 'w');
if fid < 0
    error('Cannot create inventory: %s', out);
end
cleanup = onCleanup(@() fclose(fid)); %#ok<NASGU>

fprintf(fid, 'SmartWeld source inventory\n');
fprintf(fid, 'Root: %s\n\n', root);

for k = 1:numel(files)
    f = files{k};
    fprintf(fid, 'FILE %s\n', f);
    txt = local_read_text(f);
    lines = regexp(txt, '\r?\n', 'split');
    for j = 1:min(numel(lines), 80)
        line = strtrim(lines{j});
        if ~isempty(regexp(line, '^function[ \t]', 'once'))
            fprintf(fid, '  %s\n', line);
        end
    end
    fprintf(fid, '\n');
end

fprintf('Inventory written to %s\n', out);
end

function files = local_list(root)
d = dir(root);
files = {};
for k = 1:numel(d)
    if d(k).isdir
        if strcmp(d(k).name,'.') || strcmp(d(k).name,'..')
            continue;
        end
        sub = local_list(fullfile(root,d(k).name));
        files = [files sub]; %#ok<AGROW>
    elseif length(d(k).name) >= 2 && strcmpi(d(k).name(end-1:end), '.m')
        files{end+1} = fullfile(root,d(k).name); %#ok<AGROW>
    end
end
end

function txt = local_read_text(path)
fid = fopen(path, 'r');
if fid < 0
    txt = '';
    return;
end
c = onCleanup(@() fclose(fid)); %#ok<NASGU>
txt = fread(fid, '*char')';
end
