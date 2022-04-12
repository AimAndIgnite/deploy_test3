# -*- coding: utf-8 -*-
"""deploy test3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VX-PUt5SJCZQW6dqJQ6DvQdtlp3q9SfS
"""
import sklearn
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import xgboost as xgb

data = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

st.header('Iris Classification Model Deployment Test')

st.subheader('Datasets')

if st.checkbox('Show Iris Dataset'):
    data

X = data.iloc[:, 0:4]

if st.checkbox('Show Training Dataset'):
    X.values

y = data.iloc[:, 4]

if st.checkbox('Show Testing Dataset'):
    y

# XGB model 
X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size=0.3, random_state=1)
xgb_c = xgb.XGBClassifier(max_depth=5, learning_rate=0.1, n_estimators=100, random_state=1)
xgb_c.fit(X_train, y_train)
predictions = xgb_c.predict(X_test)
accuracy = accuracy_score(predictions, y_test)

st.write('Testing accuracy: ', accuracy*100, '%')

# input 
input1 = st.slider('Sepal Length (cm)', 0.0, max(data["sepal.length"]), 1.0)
input2 = st.slider('Sepal Width (cm)', 0.0, max(data["sepal.width"]), 1.0)
input3 = st.slider('Petal Length (cm)', 0.0, max(data["petal.length"]), 1.0)
input4 = st.slider('Petal Width (cm)', 0.0, max(data["petal.width"]), 1.0)

type(input1

# predict = xgb_c.predict(input1, input2, input3, input4)

# st.write(predict)
