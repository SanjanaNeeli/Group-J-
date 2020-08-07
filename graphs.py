# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:06:28 2020

@author: DJaelee
"""
#Modules
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

#Data obtaining
datadir = Path("B-1")
F = np.load(datadir / "F.npy")
Fneu = np.load(datadir / "Fneu.npy")
spikes = np.load(datadir / "spikes.npy")
frame_info = pd.read_csv(datadir / "frame_info.csv", index_col = 0)

#Write which individual cell you want to investigate here from 0 to 200
cell_ID = 14

#Figure building
fig, ax = plt.subplots(4)
fig.suptitle('Repeated Pattern')
fig.tight_layout(pad=-.3)

#set_xlim is based on the event_info excel file. 
#Based on what you want to graph, put the frame intervals for a pattern
#into the parentheses of "set_xlim" then change label accordingly.
ax[0].plot(spikes[cell_ID], label = "ABCD")
ax[0].set_xlim(3,19)
ax[1].plot(spikes[cell_ID], label = "ABCD")
ax[1].set_xlim(34,50)
ax[2].plot(spikes[cell_ID], label = "ABBD")
ax[2].set_xlim(8113,8129)
ax[3].plot(spikes[cell_ID], label = "DCBA")
ax[3].set_xlim(14640,14656)

#Below puts up the label and actually plots
ax[0].legend()
ax[1].legend()
ax[2].legend()
ax[3].legend()
plt.ylabel('Activity')
plt.xlabel('frame')
plt.show()

#Below you can determine how similar or unsimilar two responses were.
#The lower the error value, the more similar the responses.
#The values in [:] should be put in from the same intervals 
#in the plot above for the two graphs you want to compare.
#Note that this is a VERY crude mean squared error value!
y_init = spikes[cell_ID][3:19]
y_test = spikes[cell_ID][14640:14656]
print(mean_squared_error(y_init, y_test))

