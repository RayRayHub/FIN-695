# Import libraries
import pandas as pd
import numpy as np

# Load the data
train = pd.read_csv("train.csv")
print(train.info())
test = pd.read_csv("test.csv")
print(test.info())

# eye ball data
train.head(10)
test.tail(5)

# Types of data columns
train.dtypes

# Summary statistics
train.describe()

# Find missing values
print(train.isnull().sum())
test.isnull().sum()

print(train.median())

# Impute missing values with mean (numerical variables)
train.fillna(train.median(),inplace=True)
test.fillna(test.mean(),inplace=True)
print(train.isnull().sum())
print(train.median())

# Impute missing values with mode(most frequent value) (categorical variables)
train.Gender.fillna("Female",inplace=True)
train.Married.fillna("No",inplace=True)
train.Dependents.fillna(train.Dependents.mode()[0],inplace=True)
train.Self_Employed.fillna(train.Self_Employed.mode()[0],inplace=True)
train.isnull().sum()

# Do the same with the test data
for i in ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']:
    test[i].fillna(test[i].mode()[0], inplace=True)

# Treatment of outliers
train.Loan_Amount_Term=np.log(train.Loan_Amount_Term)

# Create X and y

# Remove Loan_ID variable - Irrelevant
train=train.drop("Loan_ID", axis=1)
test=test.drop("Loan_ID", axis=1)

X=train.drop("Loan_Status", axis=1)
y=train.Loan_Status

# Convert categorical data to numberical data
X=pd.get_dummies(X)
train=pd.get_dummies(train)
test=pd.get_dummies(test)

# Split train data for cross validation
from sklearn.model_selection import train_test_split
x_train,x_cv,y_train,y_cv = train_test_split(X,y,test_size=0.3, random_state=42)

# Prediction models
# Logit the regression

from sklearn.linear_model import LogisticRegression

# invoke the class
logit = LogisticRegression(max_iter=5000)

# train the model
logit.fit(x_train, y_train)

# Make predictions on cv
pred_cv = logit.predict(x_cv)

#Evaluate accuracy of model
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
print(accuracy_score(y_cv,pred_cv)) #78.05% 
matrix=confusion_matrix(y_cv,pred_cv)
print(matrix)
print((18+78)/(18+78+2+25))

# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(x_train, y_train)

# make both in-sample and out of sample prredictions
dt_pred_train = dt.predict(x_train) #in sample
print(accuracy_score(y_train,dt_pred_train)) # 100%

dt_pred_cv = dt.predict(x_cv) # out of sample
print(accuracy_score(y_cv,dt_pred_cv)) # 70.73%

# Random Forest
#Fit model
from sklearn.ensemble import RandomForestClassifier
# invoke the model
rf=RandomForestClassifier(random_state=42)

# train the model
rf.fit(x_train,y_train)

#Predict values for cv data in sample
rf_pred_train=rf.predict(x_train)
print(accuracy_score(y_train,rf_pred_train))

rf_pred_cv = rf.predict(x_cv) # out of sample
print(accuracy_score(y_cv,rf_pred_cv)) # 77.23%

#Evaluate accuracy of model
accuracy_score(y_cv,rf_pred_cv) #77.23%
matrix2=confusion_matrix(y_cv,rf_pred_cv)
print(matrix2)

# (d)SUPPORT VECTOR MACHINE (SVM) ALGORITHM
from sklearn import svm

# invoke
svc = svm.SVC()

# train the model
svc.fit(x_train, y_train)

# predict on svc
y_cv_svc = svc.predict(x_cv)

# evaluate accuracy of model
print(accuracy_score(y_cv, y_cv_svc))
print(confusion_matrix(y_cv, y_cv_svc))

# NAIVE BAYES
from sklearn.naive_bayes import GaussianNB

# invoke
nb = GaussianNB()

# train the model
nb.fit(x_train, y_train)

# predict values for x cv data
pred_cv4 = nb.predict(x_cv)

# evaluate accuracy of model
print(accuracy_score(y_cv, pred_cv4))
print(confusion_matrix(y_cv, pred_cv4))

# kNN ALGORITHM
from sklearn.neighbors import KNeighborsClassifier

# invoke
kNN=KNeighborsClassifier()

# train the model
kNN.fit(x_train,y_train)

#Predict values for cv data
pred_cv_knn=kNN.predict(x_cv)

#Evaluate accuracy of model
print(accuracy_score(y_cv,pred_cv_knn)) #64.23%
print(confusion_matrix(y_cv,pred_cv_knn))

# GRADIENT BOOSTING ALGORITHM
from sklearn.ensemble import GradientBoostingClassifier

# invoke
gbm=GradientBoostingClassifier()

# train the model
gbm.fit(x_train,y_train)

#Predict values for cv data
pred_cv_gbm=gbm.predict(x_cv)

#Evaluate accuracy of model
print(accuracy_score(y_cv,pred_cv_gbm)) #78.86%
print(confusion_matrix(y_cv,pred_cv_gbm))

# Select the best based on cv
# gbm
# print out the accuracy score
print("gbm",accuracy_score(y_cv,pred_cv_gbm))
#...

#Predict values using test data (Naive Bayes)
#test = pd.read_csv("test.csv")

#How to make a prediction on test dataset?
#pred_test_nb=nb.predict(test)

#Write test results in csv file
#predictions=pd.DataFrame(pred_test_nb,columns=['predictions']).to_csv('Credit_Predictions.csv')

#Predict values using kNN
pred_test=kNN.predict(test)
#Write test results in csv file
predictions=pd.DataFrame(pred_test,columns=['predictions']).to_csv('knn_prediciton.csv')
np.unique(pred_test, return_counts=True)


print())
print(pred_test[-1,0].count("N"))

