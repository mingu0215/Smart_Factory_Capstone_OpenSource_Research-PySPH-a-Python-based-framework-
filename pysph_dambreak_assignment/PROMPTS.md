# PROMPTS.md

# AI Coding Tools Practice - Prompt Log

## Project Overview

This project reproduces and modifies the Dam-break experiment from the PySPH paper using AI Coding Tools.

The main objective was not only to review the paper, but also to implement and execute the experimental part of the paper by using ChatGPT as an AI coding assistant.

The implementation process included:

- PySPH environment setup
- Dam-break experiment reproduction
- Code structure analysis
- Parameter modification experiments
- Output visualization
- Dependency and viewer issue debugging

---

# AI Usage Strategy

ChatGPT was used for:

1. Understanding the PySPH architecture
2. Explaining SPH equations and execution flow
3. Designing the implementation structure
4. Generating experimental modification ideas
5. Debugging installation and execution errors
6. Building visualization and post-processing code
7. Organizing the final report structure

---

# Prompt Log

---

## Prompt 1 - Understanding the Paper and Framework

### Prompt

"Explain the PySPH paper from an implementation perspective, focusing on how Python-based SPH simulation is executed internally."

### AI Response Summary

- PySPH uses Python as a high-level simulation description language
- Equation and Integrator structures are converted into Cython/OpenMP code
- SPHCompiler generates compiled execution modules
- NNPS is used for neighbor particle search

### Actual Usage

This explanation helped analyze:

- create_particles()
- create_equations()
- create_solver()
- Equation.loop()

inside the Dam-break implementation.

---

## Prompt 2 - PySPH Installation and Environment Setup

### Prompt

"Explain how to install and execute the Dam-break example from the PySPH paper."

### AI Response Summary

- Python 3.10 + conda environment recommended
- PySPH installation using pip
- Execution using:
  python dam_break_baseline.py
- Viewer execution using:
  pysph view output_folder

### Actual Usage

Used to:

- create conda environment
- install PySPH
- execute baseline simulation
- generate output files

---

## Prompt 3 - Dam-break Code Structure Analysis

### Prompt

"Explain the Dam-break code structure based on create_particles(), create_equations(), and create_solver()."

### AI Response Summary

- create_particles() generates fluid and solid ParticleArrays
- create_equations() defines EOS, ContinuityEquation, and MomentumEquation
- create_solver() defines kernel, integrator, dt, and tf
- Equation.loop() performs neighbor particle interaction

### Actual Usage

Used to implement:

- dam_break_baseline.py
- particle initialization
- SPH equation groups
- solver configuration

---

## Prompt 4 - Parameter Modification Experiment

### Prompt

"Recommend meaningful parameters to modify for the Dam-break experiment."

### AI Response Summary

Recommended parameters:

- dx (particle spacing)
- gravity
- fluid block size

The response explained how these parameters affect:

- particle count
- runtime
- free-surface behavior
- wall impact strength

### Actual Usage

Implemented:

- dam_break_dx_modified.py
- dam_break_gravity_modified.py

and compared runtime and particle count changes.

---

## Prompt 5 - Runtime and Engineering Issues

### Prompt

"Explain possible implementation issues such as runtime increase, OpenMP behavior, dt instability, and viewer errors."

### AI Response Summary

- smaller dx increases neighbor interaction cost
- large dt may cause numerical instability
- OpenMP speedup is limited by memory and synchronization overhead
- pysph view depends on mayavi/vtk GUI packages

### Actual Usage

Used to:

- analyze runtime differences
- understand neighbor search overhead
- explain engineering limitations in the report
- replace viewer with matplotlib visualization

---

## Prompt 6 - Visualization and Post-processing

### Prompt

"Create a matplotlib-based visualization code for PySPH output files."

### AI Response Summary

- load .npz output files
- extract fluid particle arrays
- visualize density using matplotlib scatter plot

### Actual Usage

Implemented:

- visualize_output.py

and generated result figures for:

- baseline
- dx modified
- gravity modified experiments

---

## Prompt 7 - Dependency and Viewer Error Debugging

### Prompt

"Explain how to solve PySPH installation and viewer execution errors on macOS."

### AI Response Summary

- Python 3.12 compatibility issue
- Xcode SDK/compiler path problem
- mayavi/traits dependency issue

Suggested solutions:

- Python 3.10 conda environment
- reinstall Xcode CommandLineTools
- use matplotlib post-processing instead of GUI viewer

### Actual Usage

Resolved:

- cyarray build error
- compiler issue
- pysph view execution problem

---

# Major Experimental Results

| Experiment | Fluid Particles | Runtime |
|---|---|---|
| Baseline | 231 | 0.25 sec |
| DX Modified | 861 | 0.67 sec |
| Gravity Modified | 231 | 0.30 sec |

Main observations:

- Smaller dx increased particle count and runtime
- Increased gravity accelerated collapse behavior
- Free-surface motion was successfully reproduced

---

# Engineering Challenges

Main implementation challenges included:

- dependency installation
- compiler configuration
- GUI viewer issues
- runtime increase caused by particle interaction growth

The project showed that AI Coding Tools can assist not only with code generation, but also with simulation understanding, debugging, and experimental analysis.

---

# Final Outcome

Using AI Coding Tools, the PySPH Dam-break experiment from the paper was successfully:

- reproduced
- modified
- executed
- visualized
- analyzed

The project demonstrated how high-level Python SPH descriptions are transformed into executable HPC-style simulation workflows.