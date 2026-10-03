# SmartWeld / ML_SmartMelting — repository review and handoff
Review date: 2026-10-03
Repository: https://github.com/lukasjl/ML_SmartMelting

## Review scope and conclusion
Reviewed the default-branch tree, README, initial data schema and research plan, open pull requests, PR #2 changed-file patch, commit/status metadata, and recent workflow-run metadata.

The default branch main is a research-framework skeleton: README, docs/DATA_SCHEMA.md, docs/RESEARCH_PLAN.md, and placeholder files in src, tests, notebooks, simulations and experiments. Substantive SmartWeld work is in draft PRs and is not merged into main.

PR #2, “feat: build verified SmartWeld OSLW backend,” is open and draft. It adds a Windows/MATLAB backend approach, source-inspection workflow, InssTek MX-Grande mapping, and backend/data-generator documentation. Its description explicitly retains original-GUI numerical regression as a gate before DOE/ML generation. The latest surfaced source-inspection workflow succeeded, but this does not prove numerical backend regression. The status endpoint returned no individual status entries.

PR #1, “feat: integrate SmartWeld as a physics-based data generator,” is also open/draft. Compare its changed files and commits with PR #2 before merging; avoid duplicated or divergent implementations.

## Technical and scientific review findings
1. Source recovery and source inspection are evidenced; end-to-end numerical execution on Windows/MATLAB remains a distinct validation requirement.
2. Two historical GUI cases are documented. The JSON fixture is a transcription of one GUI case, not an independently recalculated expected value. Preserve that provenance.
3. Exact inverse GUI reproduction remains incomplete because ccontours.m is unresolved.
4. OSLW is a laser-welding model, not a validated powder-fed DED model. Do not equate weld width/penetration with deposited bead width/height or claim native powder-feed, catchment, nozzle, or layer-history support.
5. Synthetic SmartWeld outputs, experimental observations, simulation outputs and ML predictions must remain separately labeled and traceable.
6. Preserve original units, source table/figure/page, extraction method, replicate identity and uncertainty in literature data. Prevent leakage with grouped/source-held-out evaluation.
7. Retain third-party SmartWeld source outside the repository unless distribution/licensing review permits committing it. The PR’s checksum-verified download workflow is a sensible provenance approach.
8. The preprint is a v0.1 draft. Audit references, parameter domain, output scaling, equation-to-source traceability and broader regression coverage before submission. No ML improvement or DED transfer result is established.

## Recovered OSLW equation summary
For 304 stainless steel / argon:
- Normalization: sP=P/1600, sV=V/120, sd=d/0.0294.
- Material terms: alpha_s=5.18/110, delta_h_s=9.41/11.8.
- Argon coefficients: C1=0.9015503591510303, C2=0.6327730407815897, C3=0.2582188708198456, C8=29.32835498219138, C9=0.2903225193306445, C10=0.3160507149639552.
- Penetration: ps=alpha_s*C8*(sP/(sd^C10*sV^C9))/5.
- Energy-transfer efficiency: eta_ET_s=(C1-C2^(pi/(2*atan(C3*sd/ps))))/0.952.
- Ry_s=sP*eta_ET_s*sV/(alpha_s^2*delta_h_s); Ry=Ry_s*(1600*120*0.952)/(110^2*11.8).
- Melting efficiency: eta_m=0.48-0.29*exp(-Ry/6.82)-0.17*exp(-Ry/58.8).
- Area intermediate: As=Ry*eta_m*alpha_s^2/sV^2; A=As*(110/120)^2.
- Penetration sensitivity: dp/dP=alpha_s*C8/(1600*sd^C10*sV^C9).

Caution: final weld-width output scaling is source-defined in queryfunc. Do not infer final width from the area intermediate without preserving source scaling and units.

## Historical GUI cases
Both cases: 304 stainless steel, argon, spot diameter 0.0118 cm.

| Quantity | Case 1 | Case 2 |
|---|---:|---:|
| Power (W) | 685.000000 | 786.666667 |
| Speed (mm/s) | 53.082625 | 52.839095 |
| Penetration (mm) | 0.999860 | 1.149791 |
| Width (mm) | 0.625687 | 0.678073 |
| ETE | 0.679181 | 0.718454 |
| Melting efficiency | 0.447787 | 0.457256 |
| Sensitivity (µm/W) | 1.459649 | 1.461599 |

These cases reproduce displayed GUI values; they do not establish global accuracy or DED transfer.

## PR and task status
- PR #2: open/draft; backend/source inspection; regression remains a gate.
- PR #1: open/draft; generator foundation; overlap review required.
- Main: framework/docs foundation only; no validated backend merged.
- Source archive SHA-256 recorded in project materials: 46714ca97f740e1430e17f0265d97e7b5a909f790ac60df91cf8d157a8fb6008.

Priority tasks:
- [ ] Compare PR #1/#2 changed-file sets and consolidate.
- [ ] Run both GUI regression cases through Windows/MATLAB batch backend; compare all five outputs.
- [ ] Add deterministic automated tests, tolerances, units and environment/version metadata.
- [ ] Recover ccontours.m or document a justified replacement and inverse-selection behavior.
- [ ] Audit material/gas/spot tables and model validity range against source.
- [ ] Formalize separate provenance labels for synthetic, experimental, simulation and ML records.
- [ ] Extract numeric DED single-track data with row-level source/table/figure provenance.
- [ ] Preserve incompatible geometry definitions as separate targets and comparability classes.
- [ ] Run source-held-out baseline ML only after curation.
- [ ] Validate DED transfer experimentally before claiming it.
- [ ] Add CI compilation of TeX and publish PDF build artifacts; archive final PDFs only after content review.

## Single-track DED literature leads
Initial screening only; numeric row extraction, table/figure verification and deduplication remain incomplete.

| Material/process | Source lead | Reported data indicated in screening | DOI |
|---|---|---|---|
| Ti-6Al-4V LDED (2024) | Gonnabattula et al.; 64 conditions, 0.6 mm spot | width, depth, height, dilution | 10.1016/j.optlastec.2024.110861 |
| AISI 316L powder DED (2023) | Single-track parameter study | power/speed/feeder rotation, deposition efficiency/contact angle | 10.1016/j.procir.2023.06.126 |
| Ti-6Al-4V annular ALMD (2023) | Zhang et al.; 18 single-factor groups | 700–1200 W, 3–8 mm/s, defocus, width/height/fusion depth/thermal history; separate beam stratum | 10.3390/ma16114062 |
| 316L powder LMD (2019) | Factorial DOE | 20 mm tracks, surface and cross-section geometry | 10.3390/met9111160 |
| Ti-6Al-4V DED (2018) | Single-track layer-thickness study | power/speed combinations and cross-section morphology; DOI needs verification | DOI pending |
| Inconel 718 LMD (2020) | Baraldo et al., Zenodo dataset | power 200–700 W, speed 300–1050 mm/min, powder 0.032 g/s, synchronized track/image CSV | 10.5281/zenodo.3978982 |
| AISI 316L laser beam DED (2025) | Data in Brief; 45 tracks | width, height, area, catchment and particle stream | 10.1016/j.dib.2025.111887 |
| 316L-Si LMD (2022) | Geometry prediction/experimental validation | geometry; verify feeder units, including rev/min vs mass flow | 10.1007/s12540-022-01243-3 |
| 316L LMD (2024) | L9 optimization; 9 runs | power/speed/feed, width/height/penetration | 10.1051/mfreview/2024012 |
| Laser DED (2025) | Catchment/track-height prediction + Figshare | catchment efficiency and height | 10.1016/j.jmapro.2025.01.039; data 10.1184/R1/26065804 |
| 304L LMD (2025) | Cost-effective process study | screen for isolated single tracks; DOI/source verification pending | pending |

Recommended row schema:
source_id, DOI, material, process_family, beam_profile, laser_power_original, power_unit, laser_power_W, travel_speed_original, speed_unit, travel_speed_mm_s, spot_definition, spot_original, spot_unit, spot_mm, powder_feed_original, powder_feed_unit, powder_feed_g_s, gas, gas_flow_original, standoff_mm, substrate, preheat_C, track_length_mm, bead_width_mm, bead_height_mm, fusion_depth_mm, dilution, catchment_efficiency, replicate_id, measurement_method, uncertainty, source_table_figure_page, extraction_method, comparability_class, notes.

Retain source units and add normalized columns. Keep fusion depth, bead height, bead width, penetration, dilution and catchment distinct. Mark plot-digitized values and uncertainty. Split ML evaluation by source/build/condition.

## Materials included in this update
- docs/research/01_logbook.tex — research logbook.
- docs/research/02_preprint_draft.tex — preprint v0.1 source.
- data/regression/smartweld_oslw_regression_case.json — Case 1 fixture.
- docs/research/REPOSITORY_REVIEW_AND_HANDOFF.md — this review and project status.
- docs/research/SINGLE_TRACK_DED_SCREENING.md — literature screening register and extraction protocol.

Existing PDFs are in the project Library but are not included as binary files by this update. Compile the TeX sources to regenerate PDFs; a rebuild should not be represented as the exact archived PDF without checking its version.
