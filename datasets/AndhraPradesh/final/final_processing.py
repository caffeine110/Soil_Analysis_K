#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 01:44:25 2018


"""




import pandas as pd

filePath_Crop_Type = 'datasets/AndhraPradesh/soil_and_crops/CROPS.csv'
df_crops = pd.read_csv(filePath_Crop_Type, usecols=['Crop_before'])


filePath_Soil_Types = 'datasets/AndhraPradesh/soil_and_crops/SOIL.csv'
df_soil = pd.read_csv(filePath_Soil_Types, usecols=['Soil_type'])


filePath_soil_parameters = 'datasets/AndhraPradesh/soil_parameters.csv'
df_para = pd.read_csv(filePath_soil_parameters, usecols=['Latitude','Longitude','Avail-Cu','Avail-Mn','pH','EC','Avail-P','Exch-K','Avail-Ca','Avail-Mg','Avail-Zn','Avail-Fe','Soil_type','Crop_before'])

df_para['Soil_type'] = df_soil['Soil_type']
df_para['Crop_before'] = df_crops['Crop_before']


Final_CSV = 'datasets/AndhraPradesh/Final.csv'
df_para.to_csv(Final_CSV, index=False)




