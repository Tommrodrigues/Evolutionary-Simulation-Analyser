# Evolutionary-Simulation-Analyser

The script will analyse a log file from the [REvoSim](https://onlinelibrary.wiley.com/doi/full/10.1111/pala.12420), which simulates evolution over geological times-scales, and is used to investigate evolutionary patterns in the fossil record.

Every 50 simulated years, REvoSim outputs a data line for each species alive at that point. This means that most species (except very short-lived ones) will appear on more than one line in the log. Each species in the simulation will have evolved from one particular other species (except the initial starting species with ID `0`).

The question is: do species with bigger populations generate more daughter species? 

To answer this question, the script reads in a large `species_data.csv` file from REvoSim, and outputs a `.csv` with all the species, their maximum population size, and their daughter species count. This data can then be further analysed for correlations between population size and daughter species.

## Usage

Download with:
```
git clone https://github.com/Tommrodrigues/Evolutionary-Simulation-Analyser.git
```

Run from same directory with:
```
python3 evolution.py
```

After running the script, the analysed data will be outputted to `output.csv`.

