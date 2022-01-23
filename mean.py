import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Games.csv')
print(df['Sales'].min())
print(df['Sales'].max())
print(df['Sales'].mean())
print(df['Sales'].median())
print(df[df['Sales']>41]['Name'])
print(df[df['Sales']<2]['Name'])
print(df[df['Publisher']=='Electronic Arts']['Name'])
print(df[df['Release']=='Jun-09']['Name'])
for data in df['Release']: