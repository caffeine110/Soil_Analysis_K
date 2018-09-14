#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:37:47 2018

@author : gaurav gaurav
        : caffeine110
        
AIM     : To Analyse the soil Data in Karnataka State and its compatibility, fertility, and predict the best fit crop for that soil
        : Final year Project of Compoter Engineering

"""

import pandas as pd
import os




field_names = ['card_no', 'farmer_number', 'sau', 'state', 'district', 'taluk',
       'village', 'farmer_name', 'survey_number', 'soil_type', 'authority',
       'ph', 'ec', 'oc', 'av_p', 'av_k', 'av_s', 'av_zn', 'av_b', 'av_fe',
       'av_cu', 'av_mn' ]



filepath = 'original_details.csv'
df = pd.read_csv(filepath, usecols = ['soil_type','ph', 'ec', 'oc', 'av_p', 'av_k', 'av_s', 'av_zn', 'av_b', 'av_fe','av_cu', 'av_mn'])


df.to_csv('soilparameters.csv', index = False)