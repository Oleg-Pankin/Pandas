import pandas as pd
df = pd.read_csv('LOL Stats 12.1.csv',sep = ';')
print(df.info())
df.fillna('n',inplace = True)
print(df.info())