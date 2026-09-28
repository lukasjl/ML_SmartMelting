# Data Schema — Initial Specification

## Purpose

Define a minimum common schema for experimental and simulation data before model development.

## Required metadata

- material;
- machine/process configuration;
- laser source and nominal characteristics;
- shielding-gas configuration;
- coordinate convention;
- measurement timestamp or experiment identifier;
- units;
- acquisition/simulation software version where available;
- provenance and source identifier.

## Process parameters

Parameters should be stored with explicit units and uncertainty where known. Examples include laser power, scan speed, feed rate, layer/track identifiers, and trajectory information.

## Observations

Each measured or simulated quantity should specify:

- variable name;
- physical meaning;
- unit;
- sensor or simulation source;
- sampling rate or spatial resolution where applicable;
- uncertainty or quality flag when available.

## Dataset versions

Dataset revisions should be identifiable by immutable version identifiers or manifests. Train/validation/test partitions must be recorded rather than regenerated implicitly.