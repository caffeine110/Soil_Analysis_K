## AIM : 
Evaluation of predictive data mining alg orithms in soil data classification for opimized crop recomandation.

## Introduction
It very Hard to recomand the best fit crop for the perticular soil using traditional methods, so we can use Machine Learning and Deep Learning Algorithms to classify Crops upon Described Feature.
Datasets of soil parameters of perticular georaphical region is avilable on various server sites, and gov of india also provides soil health data which we can use to fit the model.


## Keywords 
Keywords : Machine Learning, Data Analysis, Satastics, DNN, Numpy, Pandas.

## Tools
PreRequirements :

		 LIBRARIES 	: Pandas,Numpy, Sklearn, Keras, TensorFlow, matplotlib, csv.
		 IDE 		: spyder



## Evaluation Plan
As this is a Classification Problem we can calculate the accuracy of model from sklearn.metrics using accuacy Score and Confusion Metrix.


### key Metrics :

Train on 3027 samples, validate on 757 samples
	Epoch 1/100
	3027/3027 [==============================] - 1s 452us/step - loss: 1.9017 - acc: 0.3759 - val_loss: 1.5331 - val_acc: 0.4227

	Epoch 54/100
	3027/3027 [==============================] - 1s 221us/step - loss: 0.9772 - acc: 0.6069 - val_loss: 1.0026 - val_acc: 0.6063

	Loss decreased from 1.9017 to 0.9772
	Validation Loss decreased from 1.5331 to 1.0026

	Accurcy increased from 0.3759 to 0.6069
	Validation Accuracy increased from 0.4227 to 0.6063


## Optimisation :

### Parameter Tuning

We have tued the Parameters from the 

	Train-Test split : 70-30

	Varing from 1... we choose Dense Layers : 2

	Number of Neurons in Layer each layers :
	We got best accuracy at layers at :
		: 15 Neurons at input layer as Parameters are 15
		: 15 Neurons at First Hidden layer
		: 15 Neurons at Second Hidden layer
		: 15 Neuron at output layer as there 15 classes of crops

	Tuned No of epoches 0 to 100 applied the Early_Stopping to stop model Training at paitence 3
	Batch size 8
