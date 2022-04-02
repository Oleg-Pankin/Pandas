import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


def learn_predict(df):
    x = df.drop("result", axis=1)
    y = df["result"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    classifier = KNeighborsClassifier(n_neighbors=4)
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)

    percent = accuracy_score(y_test, y_pred) * 100
    return percent, df



df = pd.read_csv('train.csv')
df.drop('bdate',axis=1,inplace=True)
df.drop('has_photo',axis=1,inplace=True)
df.drop('has_mobile',axis=1,inplace=True)
df.drop('followers_count',axis=1,inplace=True)
df.drop('graduation',axis=1,inplace=True)
df.drop('relation',axis=1,inplace=True)
df.drop('city',axis=1,inplace=True)
df.drop('occupation_name',axis=1,inplace=True)
df.drop('occupation_type',axis=1,inplace=True)
df.drop('last_seen',axis=1,inplace=True)
df.drop('education_status',axis=1,inplace=True)
df.dropna(inplace=True)
def set_career_start(value):
    if value['career_start'] =='False':
        return 0
    else:
        return 1
df['career_start'] = df.apply(set_career_start, axis=1)
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
df[list(pd.get_dummies(df['life_main'], prefix='life_main').columns)]=pd.get_dummies(df['life_main'])
df.drop('life_main',axis=1,inplace=True)
df[list(pd.get_dummies(df['people_main'], prefix='people_main').columns)]=pd.get_dummies(df['people_main'])
df.drop('people_main',axis=1,inplace=True)
df[list(pd.get_dummies(df['education_form']).columns)]=pd.get_dummies(df['education_form'])
df.drop('education_form',axis=1,inplace=True)


res,data = learn_predict(df)
print(res)
print('\n')
print(data)