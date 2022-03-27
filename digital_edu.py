import pandas as pd
df = pd.read_csv('train.csv')
a = df['langs']
df.drop('id',axis=1,inplace=True)
df.drop('bdate',axis=1,inplace=True)
df.drop('has_photo',axis=1,inplace=True)
df.drop('has_mobile',axis=1,inplace=True)
df.drop('followers_count',axis=1,inplace=True)
df.drop('graduation',axis=1,inplace=True)
df.drop('education_form',axis=1,inplace=True)
df.drop('relation',axis=1,inplace=True)
df.drop('life_main',axis=1,inplace=True)
df.drop('people_main',axis=1,inplace=True)
df.drop('city',axis=1,inplace=True)
df.drop('occupation_name',axis=1,inplace=True)
df.drop('last_seen',axis=1,inplace=True)
df.dropna(inplace=True)
def set_occupation_type(value):
    if value['occupation_type'] =='university':
        return 1
    else:
        return 0
df['occupation_type']=df.apply(set_occupation_type,axis=1)
def set_career_start(value):
    if value['career_start'] =='False':
        return 0
    else:
        return 1
df['career_start'] = df.apply(set_career_start, axis=1)
def set_education_status(value):
    if value['education_status'] =='PhD':
        return 1
    else:
        return 0
df['education_status'] = df.apply(set_education_status, axis=1)
def set_langs(value):
    if value['langs'] =='English':
        return 1
    else:
        return 0
df['langs'] = df.apply(set_langs, axis=1)
def career_end(value):
    if value['career_end'] =='False':
        return 0
    else:
        return 1
df['career_end'] = df.apply(set_career_start, axis=1)
df([list(pd.get_dummies