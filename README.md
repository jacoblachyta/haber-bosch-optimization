# Computational Optimization of the Haber–Bosch Process

## Overview

This project explores how temperature and pressure affect ammonia production in the Haber-Bosch process. I am using Python to model the reaction and investigate how different operating conditions affect the equilibrium composition.

## Reaction

N₂ + 3H₂ ⇌ 2NH₃

## Project Goals

1. Calculate how the equilibrium constant changes with temperature.
2. Model the equilibrium composition of the reaction under different conditions.
3. Compare the effects of temperature and pressure on ammonia production. 
4. Explore how operating conditions can be optimized within the model. 

More goals may be added as the project develops.

## Tools

These are the tools I plan to use in this project.

- Python
- NumPy
- SciPy
- Pandas
- Matplotlib
- Git and GitHub

## Thermodynamic Model

The temperature dependence of the ammonia synthesis equilibrium constant is modeled using the integrated van 't Hoff equation, assuming constant reaction enthalpy.

The equilibrium constant at a given temperature is calculated using the following equation:
- Kp(T) = Kp,ref × exp[-(ΔH°rxn / R) × (1/T - 1/Tref)]

Reference values:

- Reference temperature: 298.15 K
- Reference equilibrium constant: approximately \(5.43\times10^5\)
- Reaction enthalpy: −92,400 J/mol of reaction as written
- Gas constant: 8.31446 J/(mol·K)
- Standard-state pressure: 1 bar

The reference equilibrium constant was calculated using standard Gibbs energies of formation from the NIST-JANAF Thermochemical Tables, using the following equation:
Kp,ref = exp(-ΔG°rxn / RTref)

## Material Balances

The reaction composition is modeled using reaction extent, which describes how far the reaction has proceeded.

The number of moles of each species is calculated using:
- N_2: n_n2 = N_N2 - extent
- H_2: n_h2 = N_H2 - 3 * extent
- NH_3: n_nh3 = N_NH3 + 2 * extent

These material balances will be used to calculate the gas composition at different stages of the reaction and will serve as the foundation for the equilibrium calculations. 

## Current Status

The project is in development. The initial thermodynamic constants and parameters have been defined, and a temperature-dependent equilibrium constant is calculated using the integrated van 't Hoff equation. Material balance equations using reaction extent have also been developed to track changes in the amounts of nitrogen, hydrogen, and ammonia as the reaction proceeds. The next step will involve determining the equilibrium composition under different operating conditions.

## Assumptions and Limitations

The initial model will use simplified assumptions. The results will represent a theoretical model of the reaction rather than a complete simulation of an industrial reactor.

- Reaction enthalpy is assumed to be constant.
- The model does not yet account for non-ideal gas behavior, catalyst kinetics, or industrial reactor design.

As the project develops, I plan on documenting additional assumptions and limitations. 
