# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 12:23:24 2020

@author: jesdai
"""
#from sklearn.datasets import fetch_mldata
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

datadir = Path("B-1")
spikes = np.load(datadir/ "spikes.npy")

spA = np.asarray(spikes) #spikes array


spA=np.transpose(spA)
newlist=[]
counter=0
print(np.shape(spA))


event_code=[]
with open (datadir / 'frame_info.csv') as csvfile:
    
    events = csv.reader(csvfile, delimiter = ',' ) 

    for row in events:
        #event_code.append(row[12])
        if "A" in row[11]:
            event_code.append(1)
            newlist.append(spA[counter])
        elif "B" in row[11]:
            event_code.append(2)
            newlist.append(spA[counter])
        elif "C" in row[11]:
            event_code.append(3)
            newlist.append(spA[counter])
        elif "D" in row[11]:
            event_code.append(4)
            newlist.append(spA[counter])
        elif "gray" in row[11]:
            event_code.append(5)
            newlist.append(spA[counter])
        #if "-" in row[11]:
            #event_code.append(0)
        counter+=1

event_code=np.array(event_code)
print(np.shape(event_code))
spA_=np.array(newlist)
print(np.shape(spA_))

#--------DATA TRAINING--------------------------------------------------------

# test_size: what proportion of original data is used for test set
train_img, test_img, train_lbl, test_lbl = train_test_split(
    spA_, 
    event_code, 
    test_size=0.2, 
    train_size=0.8, 
    random_state=122)


scaler = StandardScaler()
# Fit on training set only.
scaler.fit(train_img)
# Apply transform to both the training set and the test set.
train_img = scaler.transform(train_img)
test_img = scaler.transform(test_img)

model = LogisticRegression(solver = 'lbfgs')
model.fit(train_img, train_lbl)

# use the model to make predictions with the test data
y_pred = model.predict(test_img)
# how did our model perform?
count_misclassified = (test_lbl != y_pred).sum()
print('Misclassified samples: {}'.format(count_misclassified))
accuracy = metrics.accuracy_score(test_lbl, y_pred)
print('Accuracy: {:.2f}'.format(accuracy))

'''Misclassified samples: 829
Accuracy: 0.92'''
    
    
    
