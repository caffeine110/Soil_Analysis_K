#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:01:00 2019

@author: 
"""

import pandas as pd
import numpy as np

#import csv

filePath = 'mean_parameters/mean_parameters.csv'
df = pd.read_csv(filePath)


dff = df[df['Crop_type'] == 'groundnut']

#print(dff)
dff = dff.drop('Crop_type', axis= 1)

#print(dff)

X = dff.values
#print(X.reshape(13,1))

x = X.tolist()
#type(x)
for i in x:
    print(i)

X_true = np.array(x)
#print(X_true)

test = [1.073756,13.111439205,7.3076,0.20419851113,0.386997517,16.994856,06.0894044665,1461.48171638,275.1377171215881,13.750777171,0.93561339956,0.551166257362,11.470392332515 ]
X_test = np.array(test)


len(X_test)

difference = np.subtract(X_true, X_test)

print(difference)








