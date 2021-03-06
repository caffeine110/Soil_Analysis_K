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
               'Avail_B', 'Avail_Fe', 'Crop_type']





###############################################################################
### importing datasets
filePath = 'input/final.csv'
df = pd.read_csv(filePath, usecols = new_column_names)
df.info
df.columns
df.dtypes
df.head()

#Y = df.iloc[:,15].values
#print(Y)

X = df.iloc[:,0:16].values
print(X[0,15])



###############################################################################
### Encoding the categerical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

### lableencoding
LabelEncoder_X = LabelEncoder()
X[:,15] = LabelEncoder_X.fit_transform(X[:,15])
print(X)


### one hot encoding
onehotencoder = OneHotEncoder(categorical_features = [15])
X = onehotencoder.fit_transform(X).toarray()
print(X)

### Saperation of X and Y
Y_data = X[:, 0:15]
print(Y_data)


X_data = X[:,15:30]
print(X_data)



###############################################################################
### Spliting the data into the training and test datasets
from sklearn.model_selection import train_test_split


### split 25% with a random state 0
X_train, X_test, Y_train, Y_test = train_test_split(X_data,Y_data,test_size = 0.2, random_state = 0)


test_df = pd.DataFrame(X_train)
test_df.to_csv('input/raw_test_sample.csv', index=False)


###############################################################################
### Feature_scalling
from sklearn.preprocessing import StandardScaler

### create sc
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print(X_test)
print(Y_test)
