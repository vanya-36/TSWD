import pandas as pd 
import numpy as np 

df = pd.read_csv('Halloween Television Episodes - ep_final_halloween.csv.csv')
print(df.columns)

"""
m=[]
for i in df['ratingCount']:
	if i>=1000:
		m.append(i)
print(len(m))
"""
h = 0
nh =0
for i in df['type']:
	if i=='Halloween':
		h+=1
		#havg.append(df['rating'])
	else:
		nh+=1
print(h,nh)

bleh=[]
bleh1=[]
for i in range(24378):
	if df['type'].iloc[i]=='Halloween':
		df['rating'][i]=int(df['rating'][i])
		bleh.append(df['rating'][i])
	else:
		bleh1.append(df['rating'][i])
a=0
for i in bleh:
	a+=i
print(a/len(bleh))



"""
raymondhall=[]
raymond =[]
for i in range(24378):
	if df['type'].iloc[i]=='Halloween' and df['rating'].iloc[i]=='Everybody Loves Raymond':
		raymondhall.append(df['rating'].iloc[i])
	if df['type'].iloc[i]=='Regular' and df['rating'].iloc[i]=='Everybody Loves Raymond':
		raymond.append(df['rating'].iloc[i])
print(np.mean(raymond))
"""