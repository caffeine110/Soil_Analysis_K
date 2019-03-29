#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:50:03 2019

@author: gaurav
"""

import pandas as pd
import numpy as np


new_column_names = ['Crop_type','Avail_Cu', 'Avail_Mn' ,'pH', 'EC', 'OC',
               'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 'Avail_Zn',
               'Avail_B', 'Avail_Fe']

new_mean_cols = ['Avail_Cu', 'Avail_Mn' ,'pH', 'EC', 'OC',
               'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 'Avail_Zn',
               'Avail_B', 'Avail_Fe']


filePath = 'input/final.csv'
df = pd.read_csv(filePath, usecols = new_column_names)

def get_detail(df):    
    df.info
    df.columns
    df.dtypes
    df.head()



#df['Crop_type'].unique()
Crop_types = ['groundnut', 'horsegram', 'jonna', 'cotton', 'sunflower', 'paddy',
       'mulberry', 'potato', 'maize', 'Topica', 'blackgram', 'greengram', 'sugarcane', 'redgram']



#print(Crop_types)

import csv
file_obj = open('mean_parameters/mean_parameters.csv', 'w')

writer = csv.DictWriter(file_obj, fieldnames = new_column_names)

writer.writeheader()


for c in Crop_types:
    #print(c)

    df_crop = df[ df['Crop_type'] == c ]
    fileName = 'Unique_Crops/Crop_' + c + '.csv'
    #print(fileName)

    df_crop.to_csv(fileName, index = False)
    
    #print(df_crop)
    
    row = dict()
    row['Crop_type'] = c
    for col in new_mean_cols:
        #print(col)
        mean = df_crop[col].mean()
        row[col] = mean
    
    #print(row)

    writer.writerow(row)

