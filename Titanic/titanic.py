# -*- coding: utf-8 -*-
"""
Titanic Data Set 
"""
# This Python 3 environment comes with many helpful analytics libraries installed
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

#importing data and test train 
train_data = pd.read_csv('C:/Users/alvaro/Desktop/Titanic/train.csv')
test_data = pd.read_csv('C:/Users/alvaro/Desktop/Titanic/test.csv')

#review train_data
train_data.head()
#review train_data
test_data.head()

#loking for data null on train_data
train_data.info()
#loking for data null on test_data
test_data.info()