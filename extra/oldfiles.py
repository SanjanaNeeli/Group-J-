# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:56:40 2020

@author: myee827
"""
from pathlib import Path
import numpy as np 
# import pandas as pd
# import matplotlib.pyplot as plt 

datadir = Path('B-1')
#spikes = np.array([np.load(datadir / 'spikes.npy')])
spikes = np.load(datadir / 'spikes.npy')
cell_dict = {}
cell_id = 0

frames = 3 

# adds cell 0 first since it is 0:3 and doesn't follow the 
# convention in the for loop 
cell_0 = spikes[0, 0:3]
cell_dict.update({'cell '+ str(cell_id) : cell_0}) 

for row in spikes: 
    cell_id += 1    #increases the cell id by one, moving to the ext row
    #adds the cell data to the dictionary
    cell_dict.update({'cell '+ str(cell_id) : spikes[frames:frames+4]})
    frames +=4 #moves to the next column set

print(cell_0)
# print(cell_dict)

    
