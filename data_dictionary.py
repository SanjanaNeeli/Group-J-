# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 23:17:19 2020

@author: sneeli
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


datadir = Path("C:/Users/sneeli/Desktop/dataRISE")
spikes = np.load(datadir/ "spikes.npy")
spA = np.asarray(spikes)
print(spA.shape)

a = []
b = []
c = []
d = []
gray = []

eventChar = 1

with open (datadir / 'event_info.csv') as csvfile:
    events = csv.reader(csvfile, delimiter = ',' )
    
    for row in events:
        
        if (row[0]!="" and row[0]!=0):
            onset = int(row[2])
            
            splice = spA[:, onset:onset+4]
            
            if (eventChar==1):
                a.append(splice)
                eventChar+=1
            
            elif (eventChar==2):
                b.append(splice)
                eventChar+=1
                
            elif (eventChar==3):
                c.append(splice)
                eventChar+=1
                
            elif (eventChar==4):
                d.append(splice)
                eventChar+=1
            
            elif (eventChar==5):
                gray.append(splice)
                eventChar=1
                       

        
dict = {'A' : a,'B' : b,'C' : c,'D' : d,'gray': gray}

#print (dict)

