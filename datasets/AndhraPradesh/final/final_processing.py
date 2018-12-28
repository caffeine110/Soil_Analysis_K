#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 01:44:25 2018


"""




import pandas as pd

filePath_Crop_Type = 'soil_and_crops/CROPS_filtered.csv'
df_crops = pd.read_csv(filePath_Crop_Type, usecols=['Crop_type'])


filePath_Soil_Types = 'soil_and_crops/SOIL_filtered.csv'
df_soil = pd.read_csv(filePath_Soil_Types, usecols=['Soil_type'])



filePath_soil_parameters = 'saperation/soil_parameters.csv'

df_para = pd.read_csv(filePath_soil_parameters, usecols = ['Latitude','Longitude','Soil_type','Crop_type','pH','EC','OC','Avail_P','Exch_K','Avail_Ca','Avail_Mg','Avail_S','Avail_Zn','Avail_B','Avail_Fe','Avail_Cu,Avail_Mn' ])

df_para['Soil_type'] = df_soil['Soil_type']
df_para['Crop_type'] = df_crops['Crop_type']


Final_CSV = 'Final_ap.csv'
df_para.to_csv(Final_CSV, index=False)




