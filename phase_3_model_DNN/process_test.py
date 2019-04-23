#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Sep 13 23:37:47 2018


AIM     : Implemetation for SUMMER crops
        	: To Analyse the soil Data in Andhrapradesh State and its compatibility, fertility,
            and predict the best fit crop for that soil

0 : Topica
1 : blackgram
2 : cottan/groundnut
3 : cotton
5 : groundnut
7 : jonna
8 : maize
9 : mulberry

10 : paddy
11 : potato
12 : redgram
13 : sugarcane
14 : sunflower


"""


###############################################################################
### importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



###############################################################################
### Declearation of global fields

field_names = ['Latitude', 'Longitude', 'Soil_type', 'Crop_type', 'pH', 'EC', 'OC',
               'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 'Avail_Zn',
               'Avail_B', 'Avail_Fe', 'Avail_Cu', 'Avail_Mn']

new_column_names = ['Latitude', 'Longitude', 'Avail_Cu', 'Avail_Mn' ,'pH', 'EC', 'OC',
               'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 'Avail_Zn',
               'Avail_B', 'Avail_Fe']





###############################################################################
### importing datasets
filePath = 'input/test_soil_sample.csv'

df = pd.read_csv(filePath, usecols=new_column_names)

#df = pd.read_csv(filePath, usecols = field_names)

def get_details():
    df.info
    df.columns
    df.dtypes
    df.head()

#Y = df.iloc[:,15].values
#print(Y)

X = df.iloc[:,0:15].values





###############################################################################
### Feature_scalling
from sklearn.preprocessing import StandardScaler

### create sc
sc = StandardScaler()

X = sc.fit_transform(X)
#X = sc.transform(X)

print(X)
