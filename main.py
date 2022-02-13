import pandas as pd
df = pd.read_csv('MPR.csv')
print(df[df['camera']==(df['camera'].max())]['model'])
print(df[df['selfie']==(df['selfie'].max())]['model'])
print(df[df['audio']==(df['audio'].max())]['model'])
print(df[df['display']==(df['display'].max())]['model'])
print(df[df['battery']==(df['battery'].max())]['model'])
def convert(data):
    data.replace('$','')
    return int(data)
df['price']=df['price'].apply(convert())
print(df[df['price']==(df['price'].mean())]['model'])