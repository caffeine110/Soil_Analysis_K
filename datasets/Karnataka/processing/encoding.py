#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Created on Thu Sep 13 23:37:47 2018

@author : gaurav gaurav
        : caffeine110
        
AIM     : To Analyse the soil Data in Karnataka State and its compatibility, fertility, and predict the best fit crop for that soil
        : Final year Project of Compoter Engineering


"""



#importing 
import pandas as pd
import numpy as np
import os

filename = 'original_details.csv'
df= pd.read_csv(filename)

X = df.loc[:,:]

X[0:10]['soil_type']

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:]['soil_type'] = labelencoder_X_1.fit_transform(X[:]['soil_type'])





'''
from sklearn import preprocessing
labelEncoder_soiltype = preprocessing.LabelEncoder()

labelEncoder_soiltype.fit(df['soil_type'])
labelEncoder_soiltype.classes_

labelEncoder_soiltype.transform(df['soil_type'])
df['soil_type'] = labelEncoder_soiltype.fit_transform(df['soil_type'])
'''


"""
import pandas as pd
import numpy as np
import os

filename = 'original_details.csv'
df= pd.read_csv(filename)
df.tail()

filename = 'all_details.csv'
df= pd.read_csv(filename)
df.tail()

filename = 'user_details.csv'
df= pd.read_csv(filename)
df.tail()

filename = 'soil_parameters.csv'
df= pd.read_csv(filename)
df.tail()
"""