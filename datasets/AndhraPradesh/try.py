#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 01:44:25 2018

"""
"""
used delimiter as ;
quates for text ""

"""


import pandas as pd
import csv


filepath = 'datasets/AndhraPradesh/soil_parameters.csv'

df = pd.read_csv(filepath, delimiter=',')

df.info()
df.columns
df.count()
df.dtypes


df.head()



import random

writeFile = open('newTry.csv', 'w', newline='')


with open('all_details.csv') as csvfile:
    reader = csv.DictReader(csvfile)
        
    writer = csv.DictWriter(writeFile, fieldnames)
    writer.writeheader()
    for row in reader:
        
        row['Crop_Label'] =
        writer.writerow(row)
