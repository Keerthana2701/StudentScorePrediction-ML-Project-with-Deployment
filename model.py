# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:34:01 2020

@author: Vikee
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

student_score=pd.read_csv("student_scores.csv")
student_score.head()
student_score.info()

X = student_score.iloc[:, :-1].values
y = student_score.iloc[:, 1].values
X
y

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(X,y)

## pickle is a serilized file used for deployment

pickle.dump(lm, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
