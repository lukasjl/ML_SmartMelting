# SmartWeld as a Synthetic Data Generator

## Purpose

SmartWeld is treated as a physics-based numerical source for generating structured training data for the ML Smart Melting research program.

The generator must preserve a strict distinction between:

1. **SmartWeld-generated numerical data**;
2. **experimental measurements**;
3. **ML-derived predictions**.

SmartWeld output must never be presented as experimental data.

## Role in the ML pipeline

The intended workflow is:

```
Process parameters
      |
      v
SmartWeld numerical model
      |
      +--> thermal / melt-pool descriptors
      |
      +--> process-state features
      |
      v
Synthetic labelled dataset
      |
      v
ML surrogate / physics-informed ML
      |
      v
prediction + uncertainty
      |
      v
experimental validation
```

The purpose is to enlarge the training space, provide physically structured priors, and reduce the amount of expensive physical experimentation required during early model development.

## Input space

The generator should accept a versioned process-parameter schema. Candidate variables include laser power, scan speed, material/feed conditions, spot parameters, and shielding-gas/process settings where these are supported by the actual SmartWeld model.

Only parameters that are demonstrably accepted by the available SmartWeld implementation should be enabled.

## Output space

The first generator version should export only quantities that are actually produced by SmartWeld or can be calculated unambiguously from its output.

Potential output classes include thermal fields, melt-pool geometry descriptors, temperature-related quantities, and process-quality indicators.

Every output must carry a provenance field identifying the SmartWeld run and model configuration.

## Dataset provenance

Each generated record should contain:

- generator name and version;
- SmartWeld version, when known;
- model/configuration identifier;
- input parameter values and units;
- output variable names and units;
- run identifier;
- random seed, if sampling is stochastic;
- timestamp;
- validity/convergence status;
- provenance hash or manifest identifier.

## Sampling strategy

The generator should support several modes:

- grid sampling for controlled studies;
- Latin hypercube sampling for space-filling datasets;
- random sampling with explicit seed;
- adaptive sampling in later stages.

Sampling ranges must be defined from validated process limits, equipment limits, literature-supported ranges, or user-supplied experimental bounds. The software must not silently invent physically valid ranges.

## Quality control

Generated records should be rejected or flagged when:

- the numerical solver fails;
- convergence is not achieved;
- required outputs are missing;
- values are outside configured physical bounds;
- units or metadata are incomplete.

Quality flags must be preserved rather than silently deleting problematic cases.

## ML split policy

Synthetic data and experimental data must remain identifiable.

Recommended initial split:

- training: SmartWeld synthetic data;
- validation: held-out SmartWeld synthetic data;
- external validation: independent experimental data.

A later mixed-data strategy can be evaluated explicitly.

## Experimental calibration

SmartWeld-generated data are intended to provide a prior/model-development dataset. Experimental observations remain necessary for calibration, validation, domain-shift analysis, and final claims about process performance.

## Implementation principle

The SmartWeld interface should be implemented as an adapter rather than embedding SmartWeld-specific assumptions throughout the ML codebase:

```
SmartWeldAdapter
      |
      +--> run()
      +--> validate()
      +--> extract_features()
      +--> export_record()
```

This allows the same ML pipeline to accept future numerical generators or experimental sources.
