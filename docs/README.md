
# Massless Gravity Research

## Overview

This project explores the concept of gravity without mass as proposed by Dr. Richard Lieu. The theory introduces shell-like topological defects that can generate gravitational effects without the need for dark matter. This repository contains theoretical developments, simulations, observational data analyses, and empirical tests to validate the proposed theory.

## Directory Structure

- **theory/**: Contains theoretical documents and Jupyter Notebooks.
  - `modified_poisson_equation.md`: Explanation of the modified Poisson equation.
  - `topological_defects.md`: Detailed description of topological defects.
  - `mathematical_models.md`: Mathematical models and derivations.
  - `potential_solutions.ipynb`: Jupyter Notebook exploring potential solutions to the gravitational field equations.

- **simulations/**: Contains simulation scripts and results.
  - `nbody_simulations.py`: Python script for N-body simulations incorporating massless shells.
  - `cosmological_simulations.py`: Python script for large-scale structure simulations.
  - `results/`: Directory containing simulation results.
    - `nbody_simulation_results.csv`: Results of N-body simulations.
    - `cosmological_simulation_results.csv`: Results of cosmological simulations.
  - `plots/`: Directory containing plots of simulation results.
    - `nbody_velocity_plot.png`: Plot of velocity profiles from N-body simulations.
    - `cosmological_structure_plot.png`: Plot of large-scale structures from cosmological simulations.

- **observational_analysis/**: Contains Jupyter Notebooks for analyzing observational data.
  - `gravitational_lensing_analysis.ipynb`: Analysis of gravitational lensing data.
  - `stellar_orbit_analysis.ipynb`: Analysis of stellar orbital velocities.
  - `data/`: Directory containing observational data.
    - `lensing_data.csv`: Gravitational lensing observational data.
    - `stellar_orbits_data.csv`: Stellar orbital velocity data.

- **empirical_tests/**: Contains Jupyter Notebooks for empirical tests.
  - `galaxy_cluster_analysis.ipynb`: Testing the theory on galaxy clusters.
  - `dwarf_galaxy_analysis.ipynb`: Testing the theory on dwarf galaxies.
  - `data/`: Directory containing data for empirical tests.
    - `cluster_data.csv`: Data from galaxy clusters.
    - `dwarf_galaxy_data.csv`: Data from dwarf galaxies.
  - `plots/`: Directory containing plots of empirical test results.
    - `cluster_gravity_plot.png`: Plot showing gravitational effects in galaxy clusters.
    - `dwarf_gravity_plot.png`: Plot showing gravitational effects in dwarf galaxies.

- **docs/**: Contains documentation and guidelines.
  - `README.md`: Overview of the project and instructions for use.
  - `changelog.md`: Record of changes and updates.
  - `contributing.md`: Guidelines for contributing to the project.
  - `license.md`: Licensing information.
  - `references.md`: List of references and citations.

- **supporting_materials/**: Contains supporting materials for the project.
  - `bibliography.bib`: Bibliographic database for LaTeX.
  - `presentation.pptx`: PowerPoint presentation summarizing findings.
  - `poster.pdf`: Research poster for conferences.

- **data_and_results/**: Contains combined data and results.
  - `summary_statistics.csv`: Summary statistics of simulation and observational data.
  - `combined_results.xlsx`: Combined results from various analyses.
  - `plots/`: Directory containing summary plots.
    - `summary_plots.png`: Summary plots for key findings.

- **project_management/**: Contains project management documents.
  - `project_plan.md`: Detailed project plan and timeline.
  - `task_list.md`: List of tasks and assignments.
  - `meeting_minutes.md`: Minutes from project meetings.

- **software_tools/**: Contains tools and scripts for setting up the project environment.
  - `requirements.txt`: List of Python dependencies.
  - `environment.yml`: Conda environment file.
  - `setup.py`: Setup script for the project.
  - `Dockerfile`: Dockerfile for setting up the project environment.

- **.github/**: Contains GitHub-specific files and workflows.
  - `workflows/`: GitHub Actions workflows for continuous integration.
    - `ci.yml`: CI pipeline configuration for automated testing and deployment.

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/massless_gravity_research.git
   ```
2. **Navigate to the project directory:**
   ```sh
   cd massless_gravity_research
   ```
3. **Set up the Python environment:**
   - Using `requirements.txt`:
     ```sh
     pip install -r requirements.txt
     ```
   - Using `environment.yml` (Conda):
     ```sh
     conda env create -f environment.yml
     conda activate massless_gravity
     ```
4. **Run the simulations or notebooks as needed.**

## Contributing

Please read `contributing.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `license.md` file for details.

## Acknowledgments

- Dr. Richard Lieu for his groundbreaking work on gravity without mass.
- The scientific community for their ongoing research and contributions to cosmology and astrophysics.
