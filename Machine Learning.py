import pandas as pd
df = pd.read_csv('train.csv')
df.drop('PassengerId',axis=1,inplace=True)
df.drop('Name',axis=1,inplace=True)
df.drop('Ticket',axis=1,inplace=True)
df.drop('Cabin',axis=1,inplace=True)
df['Enbraked'].fillna('S', inplace=True)
age_1 = df[df['Pclass'] ==1]['Age'].median()
age_2 = df[df['Pclass'] ==2]['Age'].median()
age_3 = df[df['Pclass'] ==3]['Age'].median()
df.dropna(inplace=True)
def set_gender(value):
    if value['Sex'] =='male':
        return 1
    else:
        return 0
df['Sex']=df.apply(set_gender,axis=1)
