# Research Plan — ML Smart Melting

## Working hypothesis

Laser melting and DED can be optimised more efficiently when experimental observations, numerical process models, and machine-learning surrogates are combined rather than treated as independent workflows.

## Scientific questions

1. Which process observables provide the most transferable representation of melt-pool and deposition behaviour?
2. How much experimental data can be reduced by incorporating physical priors?
3. How does uncertainty propagate from sensor and simulation inputs to predicted process quality?
4. Can adaptive experiment selection reduce the number of costly physical trials?
5. Under which constraints can reinforcement learning be used for closed-loop process optimisation?

## Baseline variables

Candidate process inputs include laser power, scan speed, feed rate, hatch/trajectory parameters, spot characteristics, shielding-gas conditions, and material descriptors.

Candidate outputs include melt-pool dimensions, temperature-related observables, deposition geometry, defects, surface quality, dilution, and process stability indicators.

Exact variables and ranges must be defined from the available experimental equipment and validated datasets rather than assumed.

## Baseline study

First implement a transparent baseline:

- data validation;
- exploratory analysis;
- physically meaningful feature construction;
- train/validation/test separation;
- baseline linear and tree-based regressors;
- one neural surrogate;
- uncertainty/error analysis;
- reproducible metrics.

Only after the baseline is reproducible should physics-informed models and reinforcement learning be introduced.

## Success criteria

Success should be evaluated against explicit baselines using held-out data and documented experimental conditions. No target performance value should be claimed before a validated dataset exists.