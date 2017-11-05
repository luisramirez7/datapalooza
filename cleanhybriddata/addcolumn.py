#This script calculates the days of growth and yield rate 
#ouputs csv of two columns to output.txt
import statistics
import pandas as pd
import numpy
from datetime import datetime

date_format = "%m/%d/%y"

f = open('clean_fix_with_allele_structure.csv', 'r')
df = pd.read_csv(f)

startdate = df['Date Planted'].tolist()
enddate = df['Date Harvested'].tolist()
yields = df['Grain yield [bu/A]'].tolist()

daystoharvest = list()
yieldrate = list()

numrows = len(yields)

for x in range(numrows):
	a = datetime.strptime(startdate[x], date_format)
	b = datetime.strptime(enddate[x], date_format)
	totaldays = (b - a).days
	daystoharvest.append(totaldays)
	yieldrate.append( yields[x] / totaldays)

print('Median Yield Rate: {}'.format(statistics.median(yieldrate)))
print('Average Yield Rate: {}'.format(statistics.mean(yieldrate)))
print('STD Yield Rate: {}'.format( statistics.stdev(yieldrate)))

with open('output.txt', 'w') as output:
	output.write('Days to Harvest, Yield Rate\n')
	for x in range(numrows):
		output.write('{},{}\n'.format(daystoharvest[x],yieldrate[x]))
