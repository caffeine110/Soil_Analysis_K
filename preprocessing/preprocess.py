#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

@author: gaurav
"""

#importing
import pandas as pd
import os
#import csv

#dataset path
filepath = 'original_details.csv'
df = pd.read_csv(filepath)


#testing
#df.head()
#df.columns

#type(df.iloc[0][15])

            del line['card_no']
            del line['farmer_number']
            del line['sau']
            del line['state']
            del line['district']
            del line['taluk']
            del line['village']
            del line['farmer_name']
            del line['survey_number']
            del line['authority']


import csv

with open('original_details.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('soildata.csv','w') as new_file:

        field_names = ['card_no', 'farmer_number', 'sau', 'state', 'district', 'taluk',
       'village', 'farmer_name', 'survey_number', 'soil_type', 'authority',
       'ph', 'ec', 'oc', 'av_p', 'av_k', 'av_s', 'av_zn', 'av_b', 'av_fe',
       'av_cu', 'av_mn' ]
        
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names,  delimiter = ',')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line['ph'],  line['oc'])