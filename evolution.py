import csv

ids = set()
maxPopulation = {}
daughterCount = {}
speciesParent = {}

with open('species_data.csv') as csvfile:
    next(csvfile)
    readCSV = csv.reader(csvfile, delimiter=',')

    # Read each line of the .csv file and add `Species_ID` to the `ids` set
    for row in readCSV:
        Species_ID = int(row[6])
        ids.add(Species_ID)

    # Set values in the `maxPopulation` and `daughterCount` to `0` so that
    # we can compare and increment them respectively
    for id in ids:
        maxPopulation[id] = 0
        daughterCount[id] = 0

with open('species_data.csv') as csvfile:
    next(csvfile)
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        Species_ID = int(row[6])
        Species_Parent = int(row[8])
        Species_Population = int(row[9])

        # Check if the population for the species is larger than the
        # previous value added to the dictionary. If so, set the
        # dictionary value to this new value
        if Species_Population > maxPopulation[Species_ID]:
            maxPopulation[Species_ID] = Species_Population

        # As long as the species parent is not `0`, set the dictionary
        # value for this species' parent to its parent. No need to
        # worry about duplicates because it will just overwrite, and
        # a species can only have 1 parent
        if Species_Parent != 0:
            speciesParent[Species_ID] = Species_Parent

# Read in all the species-parent combinations and increment the daughter
# count for a species every time it is listed as a parent
for parent in speciesParent.values():
    daughterCount[parent] += 1

# Prepare to write to `output.csv`
with open('output.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',')

    # Write a header row to label each column
    output_writer.writerow(['Species_ID', 'Maximum_Population', 'Daughter_Count'])

    # For each species, write out its id, maximum population, and number
    # of daughter species
    for id in ids:
        output_writer.writerow([id, maxPopulation[id], daughterCount[id]])
