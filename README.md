# Recommend_Me_First_ECAF26
Recommend Me First: How the Order of Recommendations Can Lead to Unfair Outcomes for Content Creators
## Description 
This repository contains the code to run simulations provided in the paper: "How the Order of Recommendations Can Lead to
Unfair Outcomes for Content Creators". We provide the code to generate the data and do not provide the data itself as the files are extremely large. 

### 1. Generate the data
To run the code to generate the simulation data: 
```from generate_config import generate_config_files
generate_config_files(1)
```

The generated files will be saved in a new folder named `Simulation_results`. You can adjust simulation parameters directly in `generate_config.py`.

## 2. Run the simulations
Once the configuration files are generated, run the simulations with: 
```import Simulations as sim
sim.run_sims()
```
The generated files of the simulation reuslts will be saved in the folder `Simulation_results`.
### 3. Small example

See [`Configuration_simulations.ipynb`](./Configuration_simulations.ipynb), which contains a minimal setup with a worked example for generating and running the simulations.


