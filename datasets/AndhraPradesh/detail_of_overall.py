#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:17:04 2018

@author: gaurav
"""


Farmer_Data_parameters = ['Sl_no', 'Date', 'Farmer_No', 'Macro/Micro_nutrient', 'Farmer_Name',
       'District', 'Mandal', 'Village', 'Latitude', 'Longitude', 'Survey_No',
       'Soil_type', 'Fathers_Name', 'Extent_AC', 'Crop_type', 'pH', 'EC',
       'OC', 'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S',
       'Avail_Zn', 'Avail_B', 'Avail_Fe', 'Avail_Cu', 'Avail_Mn', 'Time']




field_names = ['Latitude', 'Longitude', 'Soil_type', 'Crop_type', 'pH', 'EC', 'OC',
               'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 'Avail_Zn',
               'Avail_B', 'Avail_Fe', 'Avail_Cu', 'Avail_Mn']

new_column_names = ['Latitude', 'Longitude', 'Avail_Cu', 'Avail_Mn' ,'pH', 'EC', 'OC',
               'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 'Avail_Zn',
               'Avail_B', 'Avail_Fe', 'Crop_type']



Farmer_details =['Sl_no', 'Date', 'Farmer_No', 'Macro/Micro_nutrient','Farmer_Name','District', 'Mandal', 'Village','Survey_No','Soil_type','Fathers_Name','Crop_type','Time']

Soil_parameter = ['Latitude', 'Longitude', 'Soil_type', 'Crop_type','pH', 'EC','OC', 'Avail_P', 'Exch_K','Avail_Ca','Avail_Mg', 'Avail_S','Avail_Zn', 'Avail_B','Avail_Fe', 'Avail_Cu', 'Avail_Mn' ]

User_details = ['Sl_no', 'Date', 'Farmer_No', 'Macro/Micro_nutrient','Farmer_Name','District', 'Mandal', 'Village','Survey_No','Soil_type','Fathers_Name','Crop_type','Time']


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('user_details.csv', usecols = User_details)
df.info
df.columns
df.dtypes
df.head()
