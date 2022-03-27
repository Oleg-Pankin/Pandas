import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
df = pd.read_csv('train1.csv')
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
df([list(pd.get_dummies(df['Embarked']).columns)]=pd.get_dummies(df['Embarked'])
df.drop('Embarked', axis = 1,inplace = True)
x = df.drop('Survived', axis = 1)
y = df['Survived']
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.25)
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
classifier = KNeighborsClassifier(n_neighbors= 3)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
percent = accuracy_score(y_test, y_pred) * 100
print(percent)