import pandas as pd
from collections import Counter
df = pd.read_csv('Games.csv')
counter = {}
counter = Counter(df['Release'])
res = [k for k in counter if counter[k]>2]
for something in res:
    print(df[df['Release'] == something]['Name'],something)

#print(df['Sales'].min())
#print(df['Sales'].max())
#print(df['Sales'].mean())
#print(df['Sales'].median())
#print(df[df['Sales']>41]['Name'])
#print(df[df['Sales']<2]['Name'])
#print(df[df['Publisher']=='Electronic Arts']['Name'])
#print(df[df['Release']=='Jun-09']['Name'])
#df.groupby(by = 'Content Rating')['Rating'].mean()