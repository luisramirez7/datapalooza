import pandas as pd
import numpy

def change_column_order(df, col_name, index):
	cols = df.columns.tolist()
	cols.remove(col_name)
	cols.insert(index, col_name)
	return df[cols]

def rename_columns(df, col1, col2):
	df = df.rename(columns={col1:col2, col2:col1})
	return df


def append_data(df,col1,col2,index):
	copy = df
	copy = change_column_order(copy, col2, index)
	copy = rename_columns(copy, col2, col1)
	df = df.append(copy, ignore_index=True)
	return df

f = open('slimdata.csv', 'r')
df = pd.read_csv(f)

col1 = 'First Allele'
col2 = ' Second Allele'
index = 0 #set to first allele, with second allele to the left
file_name = 'duplicateddata.csv' #results data

result = append_data(df,col1,col2,index)

result.to_csv(file_name, encoding='utf-8', index=False)