#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Sep 13 23:37:47 2018

@author : gaurav gaurav
        : caffeine110
        
AIM     : Implimetation for SUMMER crops
        	: To Analyse the soil Data in Andhrapradesh State and its compatibility, fertility, and predict the best fit crop for that soil


"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#importing datasets
df = pd.read_csv('datasets/AndhraPradesh/soil_parameters.csv')
df.info
df.columns
df.dtypes


X = df.iloc[:,0:10].values
Y = df.iloc[:,10:11].values


from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

le = LabelEncoder()
Y = le.fit_transform(Y[:,0]).reshape(-1,1)

ohe = OneHotEncoder()
Y = ohe.fit_transform(Y).toarray()
Y = Y[:, 1:]





# initialise


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
classifier.add(Dense(output_dim = 100, init = 'uniform', activation= 'relu', input_dim = 10))

#Adding the second hidden layer
classifier.add(Dense(output_dim = 150, init = 'uniform', activation='relu'))

#Adding the output layer
classifier.add(Dense(output_dim = 207, init='uniform', activation='softmax'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])

#fitting the ANN to the dataset

classifier.fit(X_train, Y_train, batch_size = 10, nb_epoch = 10)


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
Y_pred = classifier.predict(X_test)
Y_pred = (Y_pred > 0.5)

#making the confusion Metrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test,Y_pred)
