from sklearn.preprocessing import OneHotEncoder
from pandas import DataFrame
import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier

os.chdir(r'D:\Python\Kaggle竞赛\泰坦尼克幸存者')

X_train = pd.read_csv('train.csv')
y_train = X_train['Survived']
X_train = X_train.drop('Survived', axis=1)
X_test = pd.read_csv('test.csv')
X_test.drop('Ticket', axis=1, inplace=True)
X_train.drop('Ticket', axis=1, inplace=True)
# 使用drop函数取除列为‘Survived’的列
'''
所有的类别
Index(['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch',
       'Ticket', 'Fare', 'Cabin', 'Embarked'],
      dtype='object')

OneHot编码的列： PassengerId, Pclass, Name, Sex, Cabin, Ticket, Embarked

Sex列里面又离谱的中性人， 离谱？？？？？
'''

X_test.drop('PassengerId', axis=1, inplace=True)
X_test.drop('Name', axis=1, inplace=True)
X_train.drop('PassengerId', axis=1, inplace=True)
X_train.drop('Name', axis=1, inplace=True)

X_train['Cabin'].fillna('none', inplace=True)
X_test['Cabin'].fillna('none', inplace=True)
X_train['Cabin'].fillna('none', inplace=True)
# 使用fillna函数填入空缺值
# 方便OneHot编码

X_test['Fare'].fillna(X_test['Fare'].mean(), inplace=True)
scaler = MinMaxScaler()
scaler.fit(X_train['Fare'].values.reshape(-1, 1), y_train)
X_test['Fare'] = scaler.transform(X_test['Fare'].values.reshape(-1, 1))
X_train['Fare'] = scaler.transform(X_train['Fare'].values.reshape(-1, 1))


# 处理Fare， 使用最大最小值放缩

X_train = pd.get_dummies(X_train)
oriIndex = np.array(X_train.index)


X_test = pd.get_dummies(X_test)




# 线性回归求age
X_train_age = X_train.dropna(axis=0, how='any')
y_train_age = X_train_age['Age']
X_train_age.drop('Age', inplace=True, axis=1)

aftIndex = np.array(list(set(oriIndex) - set(np.array(X_train_age.index))))
X_test_age = X_train.loc[aftIndex]
X_test_age.drop('Age', inplace=True, axis=1)


linear = DecisionTreeRegressor()
linear.fit(X_train_age, y_train_age)
age = linear.predict(X_test_age)
ageaft = pd.Series(age, index=aftIndex)
X_train['Age'].fillna(ageaft, inplace=True)


aftindex = X_test['Age'].dropna(axis=0, how='any').index
X_train_test_age = pd.concat([X_test['Age'], X_test['Age'].dropna(how='any')], axis=1)
index = np.array(list(set(X_test['Age'].index) - set(aftindex)))


X = pd.concat([X_test, X_train], ignore_index=True)
X_test = X[:417].fillna(0)
X_train = X[418:].fillna(0)
linear.fit(X_train.fillna(0).fillna(0), X_train.fillna(0).fillna(0)['Age'])


logreg = LogisticRegression(max_iter=2000)
kfold = KFold(n_splits=5, random_state=0)



logreg.fit(X_train, y_train)
score = logreg.predict(X_test)

csv = DataFrame({'PassengerId': range(892, 1309), 'Survived': score})
csv.to_csv('result.csv', index=False)