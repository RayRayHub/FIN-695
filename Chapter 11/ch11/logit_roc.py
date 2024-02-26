import pandas as pd
import numpy as np

#Load data files
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")


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
x_train,x_cv,y_train,y_cv = train_test_split(X,y,test_size=0.2)

#(a)LOGISTIC REGRESSION ALGORITHM
#Fit model
# from sklearn.linear_model import LogisticRegression
# model=LogisticRegression()
# model.fit(x_train,y_train)

# Random Forest
#Fit model
from sklearn.ensemble import RandomForestClassifier
# invoke the model
rf=RandomForestClassifier(random_state=42)

# train the model
rf.fit(x_train,y_train)

from sklearn.metrics import roc_auc_score
roc_rf=roc_auc_score(y_cv,rf.predict_proba(x_cv)[:,1])
print("the AUC-ROC score for Random Forest is", roc_rf)

# plot ROC curve
from sklearn.metrics import RocCurveDisplay
import matplotlib.pyplot as plt

logit_disp = RocCurveDisplay.from_estimator(rf, x_cv, y_cv)
ax = plt.gca()
plt.show()