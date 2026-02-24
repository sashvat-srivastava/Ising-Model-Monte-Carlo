# 2D Ising Model: Metropolis-Hastings Monte Carlo Simulation

This repository contains a computational simulation of a two-dimensional ferromagnetic Ising model. It utilizes the Metropolis-Hastings Monte Carlo algorithm to explore thermodynamic phase transitions, energy minimization, and spontaneous symmetry breaking in a discrete spin lattice.

## Theoretical Foundation
The system is governed by the Ising Hamiltonian, which calculates the internal energy based on nearest-neighbor exchange interactions ($J = 1$):

$$H = -J \sum_{\langle i,j \rangle} s_i s_j$$

Because computing the exact canonical partition function for all $2^N$ microstates is computationally intractable, this simulation employs Markov Chain Monte Carlo (MCMC) importance sampling. 

### The Metropolis Criterion
The simulation dynamically explores the phase space by proposing random spin-flips:
1. Flips that lower the system's energy ($\Delta E \leq 0$) are always accepted.
2. Flips that increase the system's energy ($\Delta E > 0$) are accepted with a Boltzmann probability $P = e^{-\Delta E / k_B T}$, allowing the system to accurately simulate thermal fluctuations.



## Topological Framework: The Toroidal Array
To eliminate finite-size edge effects inherent in small grids, the $10 \times 10$ rectangular lattice is mapped onto a topological torus ($S^1 \times S^1$). By implementing Periodic Boundary Conditions (PBC) via modulo arithmetic, the simulation ensures that every spin possesses exactly four neighbors (coordination number $z = 4$). This enforces translational invariance, allowing the small array to effectively simulate a localized patch within an infinite crystal lattice.

## Evaluated Thermal Regimes
The simulation is designed to be stress-tested across three distinct thermodynamic regimes to observe macroscopic ordering:
* **Low Temperature ($T \ll T_c$):** Thermal fluctuations are suppressed, resulting in spontaneous symmetry breaking and a highly ordered, single-domain ferromagnetic state.
* **Critical Temperature ($T_c \approx 2.269$):** The exact Onsager critical temperature. The system exhibits a continuous phase transition characterized by scale-invariant, fractal-like clustering of spins.
* **High Temperature ($T \gg T_c$):** Entropy dominates the exchange interaction, resulting in a completely disordered, high-entropy paramagnetic state with net-zero magnetization.

## Repository Structure
* `main.py`: The core computational engine containing the Hamiltonian logic, toroidal neighbor mapping, and the Metropolis algorithm.
* `Ising_Model_Report.pdf`: Comprehensive technical report detailing the statistical mechanics, partition function limitations, and multi-temperature output analysis.

## Dependencies
* Python 3.x
* NumPy

---
**Author:** Sashvat Srivastava   
**Institution:** Shiv Nadar Institute of Eminence