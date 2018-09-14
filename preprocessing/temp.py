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

