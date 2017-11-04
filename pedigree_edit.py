import csv
import pandas as pd

df = pd.read_csv('hybrid_raw_switch.csv', sep=',', header=0)
pedigree = df[['Pedigree']]


first_allele = list()
second_allele = list()

for index, row in pedigree.iterrows():

	if '/' in row['Pedigree']:
		alleles = row['Pedigree'].split('/')
		first_allele.append(alleles[0])
		second_allele.append(alleles[1])
	else: 
		first_allele.append(row['Pedigree'])
		second_allele.append('NONE')

new_split_data = pd.DataFrame({'FIRST': first_allele, 'SECOND': second_allele})

print(new_split_data)
