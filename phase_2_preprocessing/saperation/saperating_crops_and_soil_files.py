#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:12:34 2018


AIM : to saperate Crops and Soil parameters for analysis


INput file : ../preprocessing/processed_soil_para.csv

output files    : only_crops.csv
                only_soil_types.csv

"""

import pandas as pd

filepath_crops = '../saperation/soil_parameters.csv'
df_crop = pd.read_csv(filepath_crops, usecols = ['Crop_type'])

filepath_to_save_only_crops = 'only_crop_types.csv'
df_crop.to_csv(filepath_to_save_only_crops, index = False)
    
    

################################################################################
############################# only soil types
import pandas as pd

filepath_soil = '../saperation/soil_parameters.csv'
df_crop = pd.read_csv(filepath_soil, usecols = ['Soil_type'])
    
    
filepath_to_save_only_crops = 'only_soil_types.csv'
df_crop.to_csv(filepath_to_save_only_crops)
