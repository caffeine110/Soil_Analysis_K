#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Sep 13 23:37:47 2018

@author : gaurav gaurav
        : caffeine110
    
AIM     : Implimentation for Kharif Season
        : To Analyse the soil Data in Karnataka State and its compatibility, fertility, and predict the best fit crop for that soil

"""



#importing the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#importing datasets
dataset = pd.read_csv('processed.csv')
dataset.info
dataset.columns

X = dataset.iloc[:,0:11].values
Y = dataset.iloc[:,11].values


#encoding the categerical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
'''
onehotencoder = OneHotEncoder(categorical_features = [0])
Y = onehotencoder.fit_transform(Y).toarray()
Y = Y[:, 0:]
'''

from keras.utils import to_categorical
Y = to_categorical(Y)


#spliting the data into the training and test datasets
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.25, random_state = 0)


#feature_scalling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


### PART 2
#importing keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

#initialisation of ANN model
classifier = Sequential()

#Adding input layer and one Hiden layer 
classifier.add(Dense(output_dim = 11, init = 'uniform', activation= 'relu', input_dim = 11))

#Adding the second hidden layer
classifier.add(Dense(output_dim = 11, init = 'uniform', activation='relu'))

#Adding the output layer
classifier.add(Dense(output_dim = 11, init='uniform', activation='softmax'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])

#fitting the ANN to the dataset

classifier.fit(X_train, Y_train, batch_size = 10, nb_epoch = 100)


###################################################################
# serialize model to JSON
 
model_json = classifier.to_json()
with open("soil_classifier.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
classifier.save_weights("model_classifier.h5")
print("Saved model to disk")

###########################################################




#### PART 3


#predicting the test set Results
Y_pred = classifier.predict(X_test)
Y_pred = (Y_pred > 0.5)

#making the confusion Metrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test,Y_pred)
