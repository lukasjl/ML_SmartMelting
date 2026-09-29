function smartweld_batch_entry()
%SMARTWELD_BATCH_ENTRY Stable bridge point for the Python adapter.
%
% This file deliberately does NOT call an undocumented SmartWeld solver.
% The original source/API must be inspected before a batch call is enabled.

infile = getenv('SMARTWELD_INPUT_JSON');
outfile = getenv('SMARTWELD_OUTPUT_JSON');

if isempty(infile) || isempty(outfile)
    error('SMARTWELD_INPUT_JSON and SMARTWELD_OUTPUT_JSON are required.');
end

error(['SmartWeld solver binding is not yet verified. ' ...
       'Run inspect_smartweld.m and bind the discovered original function ' ...
       'signature here before producing scientific results.']);
end
