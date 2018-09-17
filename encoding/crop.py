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

writeFile = open('newTry.csv', 'w', newline='')
fieldnames = ['card_no', 'farmer_number', 'sau', 'state', 'district', 'taluk',
       'village', 'farmer_name', 'survey_number', 'soil_type', 'authority',
       'ph', 'ec', 'oc', 'av_p', 'av_k', 'av_s', 'av_zn', 'av_b', 'av_fe',
       'av_cu', 'av_mn','crop' ]

with open('all_details.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['crop'] = random.choice(['Ragi', 'G.nut', 'Avare', 'Maize', 'Tur', 'Paddy', 'Castor', 'Niger', 'H.gram', 'Greengram', 'Sunflower'])
        print(row['district'], row['crop'])
        writer = csv.DictWriter(writeFile, fieldnames)
        writer.writerow(row)







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










X = df.iloc[:,:23].values
Y = df.iloc[:,22].values




for i in range(0,52833):
    








import random

for i in range(0,92833):
    X[i,22] = random.choice(['Ragi', 'G.nut', 'Avare', 'Maize', 'Tur', 'Paddy', 'Castor', 'Niger', 'H.gram', 'Greengram', 'Sunflower'])
    print(X[i,22])

df = X

filepath = 'new.csv'
np.savetxt("foo.csv", X, delimiter=",")

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