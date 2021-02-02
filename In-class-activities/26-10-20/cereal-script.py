import pandas as pd 
import numpy as np 

df = pd.read_csv('cereal.csv')
print(df.columns)

df = df.sort_values('rating',ascending=False)
for i in range(10):
	print(df['name'].iloc[i],df['rating'].iloc[i],df['sugars'].iloc[i])