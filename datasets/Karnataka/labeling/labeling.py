#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 04:22:44 2018

@author: gaurav
"""

import pandas as pd
import numpy as np

filepath = "all_details.csv"
df = pd.read_csv(filepath)

df['crop'] = ''
df.to_csv(filepath, index = False)


import csv
import random
import os
from collections import Counter

writeFile = open('newTry.csv', 'w', newline='')
fieldnames = ['card_no', 'farmer_number', 'sau', 'state', 'district', 'taluk',
       'village', 'farmer_name', 'survey_number', 'soil_type', 'authority',
       'ph', 'ec', 'oc', 'av_p', 'av_k', 'av_s', 'av_zn', 'av_b', 'av_fe',
       'av_cu', 'av_mn','crop' ]


#dist = []
#dist.append('Black Soil')

with open('all_details.csv') as csvfile:
    reader = csv.DictReader(csvfile)
        
    writer = csv.DictWriter(writeFile, fieldnames)
    writer.writeheader()
    for row in reader:
        """
        d = row['soil_type']
        if d in dist:
            continue
        else:
            dist.append(d)

        #print(dist)
        """
        
        row['crop'] = random.choice(['Ragi', 'G.nut', 'Avare', 'Maize', 'Tur', 'Paddy', 'Castor', 'Niger', 'H.gram', 'Greengram', 'Sunflower'])
        print(row['district'], row['crop'])
        writer.writerow(row)






###########################################################
# code to retun all soil types

soil_types = []
soil_types.append('Black Soil')

with open('all_details.csv') as csvfile:
    reader = csv.DictReader(csvfile)
        
    writer = csv.DictWriter(writeFile, fieldnames)
    writer.writeheader()
    for row in reader:
        d = row['soil_type']
        if d in soil_types:
            continue
        else:
            soil_types.append(d)

    print(soil_types)
    
###########################################################


###########################################################
# code to ruturn all Distirctss in Karnataka
dist = []
dist.append('Bagalgot')

with open('to_csv/complete_details.csv') as csvfile:
    reader = csv.DictReader(csvfile)
        
    writer = csv.DictWriter(writeFile, fieldnames)
    writer.writeheader()
    for row in reader:
        d = row['district']
        if d in dist:
            continue
        else:
            dist.append(d)

    print(dist)
    
###########################################################

###########################################################
# code to print all the villages in karnataka
villages = []
villages.append('Badani')

with open('all_details.csv') as csvfile:
    reader = csv.DictReader(csvfile)
        
    writer = csv.DictWriter(writeFile, fieldnames)
    writer.writeheader()
    for row in reader:
        d = row['village']
        if d in villages:
            continue
        else:
            villages.append(d)

    print(dist)
    
###########################################################



"""
filepath = "newTry.csv"
df = pd.read_csv(filepath)

df.head()

df.columns = ['card_no', 'farmer_number', 'sau', 'state', 'district', 'taluk',
       'village', 'farmer_name', 'survey_number', 'soil_type', 'authority',
       'ph', 'ec', 'oc', 'av_p', 'av_k', 'av_s', 'av_zn', 'av_b', 'av_fe',
       'av_cu', 'av_mn','crop' ]

df.columns
df.dtypes
filepath = "newTry.csv"
df.to_csv(filepath, index = False)


"""
###########################################



###############
'''
import random

for i in range(0,92833):
    df.iloc[i]['crop'] = random.choice(['Ragi', 'G.nut', 'Avare', 'Maize', 'Tur', 'Paddy', 'Castor', 'Niger', 'H.gram', 'Greengram', 'Sunflower'])
    print(df.iloc[i]['crop'])

df.head()
'''



'''
for i in df.rows:

    if df[i]['district'] == "Bagalkot":
        type(df['district'])
        
        
        df['crop'] = random.choice(['Ragi', 'G.nut', 'Avare', 'Maize', 'Tur', 'Paddy', 'Castor', 'Niger', 'H.gram', 'Greengram', 'Sunflower'])

'''

"""
df.columns
df.head()
df.info
df.dtypes

"""