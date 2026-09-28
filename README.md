# ML Smart Melting

## Physics-informed machine learning for laser melting and directed energy deposition

**Research status:** active development / research framework

This repository is the starting point for a research program on machine-learning-assisted optimisation of laser melting and Directed Energy Deposition (DED). The objective is to connect process physics, numerical simulation, experimental data, and machine learning into a reproducible optimisation workflow.

## Research objective

The central problem is to develop models that can predict and optimise melt-pool behaviour and process quality while respecting the underlying physics and operating constraints.

The initial research direction combines:

- laser-material interaction and melt-pool physics;
- thermal-fluid modelling and CFD/FEA;
- experimental process data;
- physics-informed machine learning;
- surrogate modelling;
- uncertainty-aware optimisation;
- reinforcement learning and closed-loop process control;
- digital-twin concepts for additive manufacturing.

## Initial materials and processes

The framework is intended to support multiple metallic systems and laser-processing configurations rather than a single material/process combination.

Candidate systems include Ti-6Al-4V, Inconel 718, 316L, and AlSi10Mg, subject to availability of validated experimental and simulation data.

## Conceptual architecture

```text
Experimental data ─┐
                   ├──> Data / feature layer ──> ML surrogate ──> Optimisation
Simulation / CFD ──┘                                  │
                                                       ▼
                                             Physics constraints
                                                       │
                                                       ▼
                                              Process controller
                                                       │
                                                       ▼
                                             DED / laser process
                                                       │
                                                       └── feedback
```

## Planned research layers

### 1. Data layer

Organise process parameters, sensor measurements, simulation outputs, and derived physical quantities in a reproducible format.

### 2. Physics layer

Represent thermal, fluid, geometric, and process constraints explicitly rather than treating the process as a purely black-box prediction problem.

### 3. ML layer

Evaluate regression and surrogate-model approaches, including neural networks, Gaussian processes, and other data-efficient models appropriate for limited experimental datasets.

### 4. Optimisation layer

Use Bayesian optimisation and, at a later stage, reinforcement learning for adaptive selection of process parameters.

### 5. Digital-twin layer

Integrate simulation, sensor observations, uncertainty estimation, and process-state inference into a computational representation of the manufacturing process.

## Reproducibility principles

- Keep raw and processed data conceptually separated.
- Record units and parameter definitions explicitly.
- Store train/validation/test splits deterministically.
- Record software and model versions.
- Preserve experimental provenance.
- Avoid reporting model performance without specifying the dataset and evaluation protocol.
- Prefer physics-constrained and uncertainty-aware comparisons where the data support them.

## Planned repository structure

```text
data/          # documented datasets and dataset metadata
notebooks/     # exploratory and demonstration notebooks
src/           # reusable Python research code
models/        # model definitions and configurations
experiments/   # experiment specifications and results
simulations/   # simulation interfaces and generated metadata
docs/          # scientific documentation
tests/         # automated tests
```

Generated large datasets should not be committed directly to Git unless their size and distribution conditions make that appropriate. Dataset manifests and provenance records should be preferred.

## Research roadmap

**Phase I — Foundation**

- define a common process-parameter schema;
- establish a baseline dataset;
- implement baseline regression/surrogate models;
- define physically meaningful target variables;
- establish reproducible evaluation.

**Phase II — Physics-informed modelling**

- incorporate thermal/process constraints;
- compare purely data-driven and physics-informed models;
- quantify uncertainty;
- connect simulation outputs with experimental observations.

**Phase III — Adaptive optimisation**

- Bayesian optimisation;
- active learning;
- sequential experiment selection;
- process-window exploration.

**Phase IV — Closed-loop control**

- state estimation;
- adaptive control;
- reinforcement learning under physical and safety constraints;
- digital-twin integration.

## Relation to the broader research program

This repository is intended to become the active computational component of a broader research trajectory:

**Detector instrumentation → physical modelling → laser/DED → machine learning → autonomous experimental systems**

The historical `CTOFCalibration` repository is preserved separately as an example of earlier detector-instrumentation and scientific-computing work.

## Current status

This repository was previously an empty/template repository. The present README establishes its scientific scope and development architecture; experimental code and validated datasets will be added incrementally.

## Author

Research repository associated with work on physics-informed machine learning, laser processing, additive manufacturing, and autonomous optimisation.