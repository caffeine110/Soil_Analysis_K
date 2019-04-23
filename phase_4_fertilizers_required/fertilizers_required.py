#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:01:00 2019

@author: 
"""

import pandas as pd
import numpy as np

#import csv

def get_fertilizers_required(test_soil_para):
    
    filePath = '/home/gaurav/Developer_repo/Soil_Analysis/Deployable/phase_4_fertilizers_required/mean_parameters/mean_parameters.csv'
    df = pd.read_csv(filePath)
        
    dff = df[df['Crop_type'] == 'groundnut']
    
    #print(dff)
    dff = dff.drop('Crop_type', axis= 1)
    
    #print(dff)
    
    X = dff.values
    #print(X.reshape(13,1))
    
    x = X.tolist()
    #type(x)
    
    X_true = np.array(x)
    #print(X_true)
    
    #float_test_soil_para = [ float(i) for i in test_soil_para ]
    float_test_soil_para = np.array(test_soil_para)

    X_test = np.array(float_test_soil_para)
    
    #len(X_test)

    difference = np.subtract(X_true, X_test)
    difference.reshape(13,1)
    difference = difference.tolist()

    diff = difference[0]

    return diff



test = [1.073756,13.111439205,7.3076,0.20419851113,0.386997517,16.994856,06.0894044665,1461.48171638,275.1377171215881,13.750777171,0.93561339956,0.551166257362,11.470392332515 ]

result = get_fertilizers_required(test)
print(result)
print(len(result))


