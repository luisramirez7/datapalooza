import csv
import pandas as pd

df = pd.read_csv('hybriddataset.csv', sep=',', header=0)
pedigree = df[['Pedigree']]


first_allele = list()
second_allele = list()

for index, row in pedigree.iterrows():

	if '/' in row['Pedigree']:
		alleles = row['Pedigree'].split('/')
		first_allele.append(alleles[0])
		second_allele.append(alleles[1])

new_split_data = pd.DataFrame({'FIRST': first_allele, 'SECOND': second_allele})
numrows = len(first_allele)
with open('luis_output.txt', 'w') as output:
	output.write('First Allele, Second Allele\n')
	for x in range(numrows):
		output.write('{},{}\n'.format(first_allele[x],second_allele[x]))