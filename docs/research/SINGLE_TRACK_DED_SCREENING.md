# Single-track DED literature screening register
Status: candidate bibliography only; numeric extraction incomplete. Screened 2026-10-03.

| ID | Material/process | Publication/dataset | DOI/identifier | Screening notes |
|---|---|---|---|---|
| ST-01 | Ti-6Al-4V LDED | Gonnabattula et al. (2024), 64 conditions, 0.6 mm spot | 10.1016/j.optlastec.2024.110861 | Width/depth/height/dilution; extract rows and units. |
| ST-02 | AISI 316L powder DED | Single-track parameter study (2023) | 10.1016/j.procir.2023.06.126 | Feeder rotation; do not assume mass-flow conversion. |
| ST-03 | Ti-6Al-4V annular ALMD | Zhang et al. (2023) | 10.3390/ma16114062 | 18 groups, 700–1200 W, 3–8 mm/s, defocus; separate beam stratum. |
| ST-04 | 316L powder LMD | Factorial DOE (2019) | 10.3390/met9111160 | 20 mm tracks, surface/cross-section geometry. |
| ST-05 | Ti-6Al-4V DED | Single-track layer-thickness study (2018) | DOI pending verification | Open PMC article identified; verify citation and extract. |
| ST-06 | Inconel 718 LMD | Baraldo et al. (2020), Zenodo | 10.5281/zenodo.3978982 | Power 200–700 W, speed 300–1050 mm/min, feed 0.032 g/s; inspect downloadable CSVs. |
| ST-07 | AISI 316L laser beam DED | Data in Brief (2025), 45 tracks | 10.1016/j.dib.2025.111887 | Width, height, area, catchment, particle stream. |
| ST-08 | 316L-Si LMD | Geometry prediction/validation (2022) | 10.1007/s12540-022-01243-3 | Verify feeder units, including rev/min. |
| ST-09 | 316L LMD | L9 DOE optimization (2024) | 10.1051/mfreview/2024012 | Nine-run design; power/speed/feed and geometry targets. |
| ST-10 | Laser DED | Catchment and track-height prediction (2025) | 10.1016/j.jmapro.2025.01.039; Figshare 10.1184/R1/26065804 | Download and inspect data before inclusion. |
| ST-11 | 304L LMD | Cost-effective LMD study (2025) | DOI pending verification | Confirm isolated single-track status and citation. |

## Extraction and inclusion protocol
1. Verify DOI, publication metadata, material/process, and genuinely isolated single-track design.
2. Retrieve full text, supplement and dataset; record version/access date.
3. Extract one row per condition and replicate; never infer missing values.
4. Record source table/figure/page and original units for every field.
5. Distinguish nominal from delivered power and feeder rotation from mass flow.
6. Keep bead width, deposited height, fusion depth, penetration, dilution and catchment as distinct targets.
7. For plot digitization, record software, calibration, mapping, uncertainty and digitized status.
8. Preserve source units and add harmonized columns.
9. Assign comparability classes rather than force-merging unlike processes.
10. Deduplicate repeated reports while preserving replicate structure.
11. Use grouped/source-held-out validation; prevent track/frame leakage.
12. Separate literature observations from SmartWeld synthetic output and new experiments.

No numeric experimental rows are included until extracted and source-checked.
