AIM 	: Evaluation of predictive data mining alg orithms in soil data classification for opimized crop recomandation.


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
As this is a Classification Problem we can calculate the accuracy of model from sklearn.metrics using accuacy Score.

