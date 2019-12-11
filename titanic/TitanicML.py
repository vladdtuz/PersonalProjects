'''
date: 23/09/19
author: Vlad Turculetu
Title: Machine learning on the titanic dataset
'''

import pandas as pd
from sklearn.preprocessing import OneHotEncoder 
data = pd.read_csv('titanic/train.csv')
data = data.drop(axis=1,columns='Cabin')
data = pd.get_dummies(data,columns=['Sex'])
data.drop