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


Abstraact 	: we have studied the data manipulation libraries such as Numpy and Pandas for handling the huge dataset of soil health.
		  using matplot library we can visualise all the implimented modules.
		  Using sk-learn we can import test-train split method which divides the whole data into test and train cases.
		  Using keras we can build the DNN model with Sequential layers.
		  Our Model is Built using Keras, and TensorFlow is an alternative library which allows to create ML model using Estemators and Tensors.
		  Flask is a Frame work which allows us to create WebApp and host on server.



## procedure to run
Procedure to Exicute the Program: 

	1). Exctraction :
		Dataset can download from data.com and data.gov.india and some state goverment provides data of soil health card.
	2). Preporcessing
		Run the preprocessing/preprocessing.py file to preprocess the downloaded data.
	3). Model Training
		Move to folder models/state_name and Run the models_s.py file to fit data to model.
		While the model if trained program is under exicution and after complition apply the prediction steps.
	4). prediction
		To predict the best fit crop for perticular soil sample store the soil parameters in test Pred_test cases.
		Output is shown in single variable as a name of crop


## Evaluation Plan
As this is a Classification Problem we can calculate the accuracy of model from sklearn.metrics using accuacy Score and Confusion Metrix.


### key Metrics :

	Epoch 1/100
	2838/2838 [==============================] - 2s 545us/step - loss: 0.1905 - acc: 0.9328 - val_loss: 0.1692 - val_acc: 0.9346

	Epoch 65/100
	2838/2838 [==============================] - 1s 324us/step - loss: 0.1093 - acc: 0.9527 - val_loss: 0.1117 - val_acc: 0.9531

	Loss decreased from 0.1905 to 0.1093
	Validation Loss decreased from 0.1692 to 0.1117

	Accurcy increased from 0.9328 to 0.9527
	Validation Accuracy increased from 0.9346 to 0.9531


## Optimisation :

### Parameter Tuning

We have tued the Parameters from the 

	Train-Test split from 60-40 ... 80-20 and get the best accuracy at 75-25

	Varing from 1... we choose Dense Layers : 3

	Number of Neurons in Layer each layers :
	We got best accuracy at layers at :
		: 15 Neurons at input layer as Parameters are 15
		: 15 Neurons at First Hidden layer
		: 15 Neurons at Second Hidden layer
		: 15 Neuron at output layer as there 15 classes of crops

	Tuned No of epoches 0 to 100 applied the Early_Stopping to stop model Training at paitence 4
	Batch size 8
