import pandas as pd 
import numpy as np 

df = pd.read_csv('avengers.csv')
print(df.shape)
f = 0
m = 0
for i in df['Gender']:
	if i == 'MALE':
		m+=1
	else:
		f+=1
print(f, m)

hon = 0
full = 0
acad = 0
for i in df['Honorary']:
	if i == 'Full':
		full+=1
	elif i == 'Honorary':
		hon+=1
	else:
		acad+=1
print(hon, full, acad)

df = df.sort_values('Appearances',ascending=False)
for i in range(11):
	print(df['Name/Alias'].iloc[i],df['Appearances'].iloc[i])