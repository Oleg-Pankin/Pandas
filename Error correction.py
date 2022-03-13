import pandas as pd
from collections import Counter
df = pd.read_csv('Games.csv')
print(df.info())
print(df['Sales'].mean())
print(df[df['Sales']>1.5]['Genre'])
