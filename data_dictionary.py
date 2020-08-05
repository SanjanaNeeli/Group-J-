# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:08:19 2020

@author: jesdai
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
print(spA)
#we created lists for each event
a = []
b = []
c = []
d = []
gray = []

eventChar = 1 #this is the count value that will 
#help us iterate through the rows of event_info and determine 
#what event occured (a,bc,d,gray) and append frame values
# to the respective event lists

with open (datadir / 'event_info.csv') as csvfile:
    events = csv.reader(csvfile, delimiter = ',' ) 
    
    for row in events:
        if "_r" not in str(row[1]): #removes all the reverse data
            if (row[0]!="" and row[0]!=0): 
                onset = int(row[2]) 
                #this gets the event onset value for each row in the file 
                splice = spA[:, onset:onset+4]
                #this returns the frames we want between each onset and offset
                
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
        
                       

#creates our dictionary         
dict = {'A' : a,'B' : b,'C' : c,'D' : d,'gray': gray}
print(dict)

#print (dict)
