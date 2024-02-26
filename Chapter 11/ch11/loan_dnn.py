#(1)LOADING DATA
#Import libraries
import pandas as pd
import numpy as np

#Load data files
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

#(2)DATA CLEANING AND PREPROCESSING
#Find missing values
train.isnull().sum()
test.isnull().sum()

#Impute missing values with mean (numerical variables)
train.fillna(train.mean(),inplace=True) 
train.isnull().sum() 

#Test data
test.fillna(test.mean(),inplace=True) 
test.isnull().sum()

#Impute missing values with mode (categorical variables)
train.Gender.fillna(train.Gender.mode()[0],inplace=True)
train.Married.fillna(train.Married.mode()[0],inplace=True)
train.Dependents.fillna(train.Dependents.mode()[0],inplace=True) 
train.Self_Employed.fillna(train.Self_Employed.mode()[0],inplace=True)  
train.isnull().sum() 

#Test data
test.Gender.fillna(test.Gender.mode()[0],inplace=True)
test.Dependents.fillna(test.Dependents.mode()[0],inplace=True) 
test.Self_Employed.fillna(test.Self_Employed.mode()[0],inplace=True)  
test.isnull().sum() 

#Treatment of outliers
train.Loan_Amount_Term=np.log(train.Loan_Amount_Term)

#(3)PREDICTIVE MODELLING
#Remove Loan_ID variable - Irrelevant
train=train.drop('Loan_ID',axis=1)
test=test.drop('Loan_ID',axis=1)

#Create target variable
X=train.drop('Loan_Status',1)

y=train['Loan_Status']
#Build dummy variables for categorical variables
X=pd.get_dummies(X)
train=pd.get_dummies(train)
test=pd.get_dummies(test)

#Split train data for cross validation
from sklearn.model_selection import train_test_split
x_train,x_cv,y_train,y_cv = train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# IN CLASS dnn
y_train.replace(('Y', 'N'), (1, 0), inplace=True)
X_train=x_train.to_numpy().reshape((-1, 20))
print(X_train.shape)

Y_train=y_train.to_numpy().reshape((-1, 1))
print(Y_train.shape)

X_cv=x_cv.to_numpy().reshape((-1, 20))
print(X_cv.shape)

import tensorflow as tf
dnn = tf.keras.Sequential()
dnn.add(tf.keras.layers.Dense(128,activation="relu",input_shape=(20,)))
dnn.add(tf.keras.layers.Dense(64,activation="relu"))
dnn.add(tf.keras.layers.Dense(32,activation="relu"))
dnn.add(tf.keras.layers.Dense(32,activation="relu"))
dnn.add(tf.keras.layers.Dense(16,activation="relu"))
dnn.add(tf.keras.layers.Dense(16,activation="relu"))
dnn.add(tf.keras.layers.Dense(8,activation="relu"))
dnn.add(tf.keras.layers.Dense(1, activation='sigmoid'))

dnn.compile(optimizer="adam", loss="binary_crossentropy")
dnn.fit(X_train, Y_train, epochs=50)

pred_dnn=dnn.predict(X_cv)

# Convert values between 0 and 1 to Y or N 
pred_dnn_yn = np.where(pred_dnn > 0.5, 'Y', 'N')
#print (pred_dnn_yn)
# Convert back to pd DataFrame
pred_nn = pd.DataFrame(data=pred_dnn_yn)
# Evaluate accuracy of model
accu_nn=accuracy_score(y_cv,pred_nn) 
matrix_nn=confusion_matrix(y_cv,pred_nn)
print(matrix_nn)
print("the accuracy for deep neural network algorithm is", accu_nn)




