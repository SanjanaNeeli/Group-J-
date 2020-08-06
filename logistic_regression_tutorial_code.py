# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:22:14 2020

@author: myee827
"""

#These imports are the from the tutorial but we can 
#change them to fit our data

#change some of the libraries 
import sklearn
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler 
from sklearn import metrics
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression

#import pandas as pd
import numpy as np 
from pathlib import Path
#import matplotlib.pyplot as plt 

datadir = Path('B-1')
mnist = fetch_openml('mnist_784')

print(mnist.data.shape)
#print(mnist.COL_NAMES)
print(mnist.target.shape)
print(np.unique(mnist.target))

#change this part so that it is our training data 
# test_size: what proportion of original data is used for test set
train_img, test_img, train_lbl, test_lbl = train_test_split(mnist.data, mnist.target, test_size=1/7.0, random_state=122)

scaler = StandardScaler()
# Fit on training set only.
scaler.fit(train_img)
# Apply transform to both the training set and the test set.
train_img = scaler.transform(train_img)
test_img = scaler.transform(test_img)

model = LogisticRegression(solver = 'lbfgs')

#use our data, train_img is our training data, and train_lbl is 
#the corresponding event code 
model.fit(train_img, train_lbl)

# use the model to make predictions with the test data
# rather than test_img, use the test data
y_pred = model.predict(test_img)
# how did our model perform?
count_misclassified = (test_lbl != y_pred).sum()
print('Misclassified samples: {}'.format(count_misclassified))
accuracy = metrics.accuracy_score(test_lbl, y_pred)
print('Accuracy: {:.2f}'.format(accuracy))