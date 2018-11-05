#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Sep 13 23:37:47 2018


AIM     : Implimetation for SUMMER crops
        	: To Analyse the soil Data in Andhrapradesh State and its compatibility, fertility,
            and predict the best fit crop for that soil



"""

field_names = ['Latitude', 'Longitude', 'Soil_type', 'Crop_type', 'pH', 'EC', 'OC',
               'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 'Avail_Zn',
               'Avail_B', 'Avail_Fe', 'Avail_Cu', 'Avail_Mn']

new_column_names = ['Latitude', 'Longitude', 'Avail_Cu', 'Avail_Mn' ,'pH', 'EC', 'OC',
               'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 'Avail_Zn',
               'Avail_B', 'Avail_Fe', 'Crop_type']



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#importing datasets
#df.columns
df = pd.read_csv('final.csv', usecols = new_column_names)
df.info
df.columns
df.dtypes
df.head()


X = df.iloc[:,0:16].values
print(X)

Y = df.iloc[:,16].values
print(Y)


"""
LabelEncoder_X = LabelEncoder()
X[:,15] = LabelEncoder_X.fit_transform(X[:,15])

print(X)

onehotencoder = OneHotEncoder(categorical_features = [15])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 15:]

"""

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

################
"""
LabelEncoder_Y = LabelEncoder()
Y = LabelEncoder_Y.fit_transform(Y)
print(Y)

onehotencoder = OneHotEncoder(categorical_features = [0])
Y = onehotencoder.fit_transform(Y).toarray()
Y = X[:, 0:]
"""

###############
LabelEncoder_X = LabelEncoder()
X[:,15] = LabelEncoder_X.fit_transform(X[:,15])
print(X)

onehotencoder = OneHotEncoder(categorical_features = [15])
X = onehotencoder.fit_transform(X).toarray()
print(X)


Y_data = X[:, 0:15]
print(Y_data)


X_data = X[:,15:30]
print(X_data)


# initialise

#spliting the data into the training and test datasets
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X_data,Y_data,test_size = 0.25, random_state = 0)


#feature_scalling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print(X_test)
print(Y_test)


### PART 2
#importing keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

#initialisation of ANN model
classifier = Sequential()

#Adding input layer and one Hiden layer 
classifier.add(Dense(output_dim = 15, init = 'uniform', activation= 'relu', input_dim = 15))

#Adding the second hidden layer
classifier.add(Dense(output_dim = 15, init = 'uniform', activation='relu'))

#Adding the output layer
classifier.add(Dense(output_dim = 15, init='uniform', activation='softmax'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])

#fitting the ANN to the dataset

classifier.fit(X_train, Y_train, batch_size = 10, nb_epoch = 1000)


###################################################################
# serialize model to JSON
 
model_json = classifier.to_json()
with open("soil_classifier.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
classifier.save_weights("Model_AndhraPradesh_Summer.h5")
print("Model is Saved")

###########################################################




#### PART 3


#predicting the test set Results
X_pred1 = X_test[0:5,:]
print(X_pred1)

Y_pred1 = Y_test[0:5,:]
print(Y_pred1)



Y_pred = classifier.predict(X_pred1)
Y_pred = (Y_pred > 0.5)



#making the confusion Metrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test,Y_pred)
