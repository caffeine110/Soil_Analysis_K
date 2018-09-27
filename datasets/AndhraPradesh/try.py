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

filepath = 'complete_details_ap.csv'

df = pd.read_csv(filepath, usecols=['Crop_before'])

from sklearn import preprocessing
labelEncoder_croptype = preprocessing.LabelEncoder()
labelEncoder_croptype.fit(df['Crop_before'])
labelEncoder_croptype.classes_


df.info()
df.columns
df.count()
df.dtypes



df.head()


#################################################
######################################################