#!/usr/bin/env pyth on3 Spyder Editor
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 12:06:22 2018

        
AIM     : To build Ann which predicts which Customer is most likely to leave the job
        : implimenting ANN in Sklearn

"""

###############################################################################
### importing data
def get_Data():
    ### importing data
    from process_test import X

    #return X_train, X_test, Y_train, Y_test
    return X



###############################################################################
### Building model
def build_Model():
    ### Importing keras libraries and packages
    from keras.models import Sequential
    from keras.layers import Dense

    #initialisation of DNN model
    clf_model = Sequential()

    #Adding input layer and one Hiden layer 
    clf_model.add(Dense(output_dim = 15, init = 'uniform', activation= 'relu', input_dim = 15))

    #Adding the second hidden layer
    clf_model.add(Dense(output_dim = 15, init = 'uniform', activation='relu'))

    #Adding the third hidden layer
    clf_model.add(Dense(output_dim = 15, init = 'uniform', activation='relu'))

    #Adding the third hidden layer
    #clf_model.add(Dense(output_dim = 15, init = 'uniform', activation='relu'))

    #Adding the third hidden layer
    #clf_model.add(Dense(output_dim = 15, init = 'uniform', activation='relu'))


    #Adding the output layer
    clf_model.add(Dense(output_dim = 15, init='uniform', activation='softmax'))
    clf_model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics=['accuracy'])
    
    print('\n')
    print('\n')
    print('Dense Neural Network for Crop prediction...')
    print('Model Architecture is : ')

    print(clf_model.summary())
    print('\n')
    print('\n')

    return clf_model



###############################################################################
def load_Weights(saved_model):
    saved_model.load_weights('/home/gaurav/Developer_repo/Soil_Analysis/Deployable/phase_3_model_DNN/checkpoints/my_clf_Model_weights.h5')
    return saved_model


###############################################################################
def display_CM(Y_test,Y_pred):

    Y_test = (Y_test > 0.5)
    print(Y_test)
    print(Y_pred)

    #Y_test = int(Y_test=='True')

    #making the confusion Metrix
    from sklearn.metrics import confusion_matrix
    
    #creating cofusion metrix
    #cm = confusion_matrix(Y_test, Y_pred)

    #cm = confusion_matrix(Y_test.argmax(axis=1), Y_pred.argmax(axis=1))

    print('Confusion Matrix Obtained is : ')
    print(cm)



###############################################################################
def get_Predictions(saved_model, X_test):
    Y_pred = saved_model.predict(X_test)
    #Y_pred = Y_pred > 0.5
    return Y_pred




###############################################################################
### Accuracy graph
def plot_Accuracy_Graph(Y_test, Y_pred):
    y_original = Y_test[50:100]
    y_predicted = Y_pred[50:100]
    
    ### importing matplotlib
    import matplotlib.pyplot as plt

    plt.plot(y_original, 'r')
    plt.plot(y_predicted, 'b')
    plt.ylabel('predicted-b/original-r')
    plt.xlabel('n')
    plt.legend(['predicted', 'original'], loc='upper left')

    plt.show()



###############################################################################
### Accure Scores
def accuracy_Score(Y_test, Y_pred):
    Y_test = Y_test > 0.5
    Y_pred = Y_pred > 0.4
    
    print(Y_test)
    print(Y_pred)
    from sklearn.metrics import accuracy_score
    ### Calculating the Varience Score
    acc = accuracy_score(Y_test, Y_pred)
    print('\n\n')
    print("Accuracy Score for Single Crop prediction is : ",acc)





###############################################################################
def get_best_fitting_Crop(test_soil_para):
    import numpy as np
    import pandas as pd
    
    ### function call to get data
    #X = get_Data()


    float_test_soil_para = test_soil_para
    #float_test_soil_para = [ float(i) for i in test_soil_para ]


    X = np.array(float_test_soil_para)
    X = X.reshape(1,15)
    ### function call to build MOdel
    saved_model = build_Model()
    
    saved_model = load_Weights(saved_model)
    
    Y_pred = get_Predictions(saved_model, X)
    
    print(Y_pred)
    
    
    crop_label = np.argmax(Y_pred, axis=1)
    print(crop_label)
    crop_label = crop_label.tolist()
    crop_label = crop_label[0]
    
    dictionary = { 0 : 'Topica', 1 : 'blackgram', 2 : 'cottan/groundnut', 3 : 'cotton', 5 :'groundnut',
                  7 : 'jonna', 8 : 'maize', 9 : 'mulberry' ,10 : 'paddy' ,11 : 'potato' , 
                  12 : 'redgram' ,13 : 'sugarcane' ,14 : 'sunflower' }
    
    
    crop_type = dictionary[crop_label]
    
    print(crop_type)
    
    return crop_type


#get_crop()


###############################################################################
"""
#Y_pred.argsort()[-3:][::-1]

y = list()
Y_pred = Y_pred.reshape(15,1)
y = Y_pred.tolist()

print(y)

for i in y:
    print(i)
    type(i)

"""

#test_soil_para = [1,1,1.073756,13.111439205,7.3076,0.20419851113,0.386997517,16.994856,06.0894044665,1461.48171638,275.1377171215881,13.750777171,0.93561339956,0.551166257362,11.470392332515 ]
#crop_type = get_best_fitting_Crop(test_soil_para)
#print(crop_type)
#print('EOF')
