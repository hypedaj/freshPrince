from collections import defaultdict
population_dict = defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        if line[1] == 'Total National Population':
        	population_dict[line[0]] += line[5]
