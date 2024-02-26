#Import needed libraries.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#Import data.
data = pd.read_csv("Datasets/salary_data_cleaned.csv")

#Check how many values are missing (NaN) before we apply the methods below.
count_nan = data.isnull().sum() # the number of missing values for every column

#Drop the rows that don't report a salary and instead are hourly.
data_salary = data[data.hourly != 1]

#Categorical parameters: Job Title, Type of ownership, Industry, Job_State get dummy variables.
job_title_encoded = pd.get_dummies(data_salary["Job Title"])
type_of_ownership_encoded = pd.get_dummies(data_salary["Type of ownership"])
industry_encoded = pd.get_dummies(data_salary["Industry"])
job_state_encoded = pd.get_dummies(data_salary["job_state"])

#Add categorical data to data_salary.
data_salary_encoded = pd.concat(objs=[data_salary, job_title_encoded, job_state_encoded, type_of_ownership_encoded, industry_encoded], axis=1)
count_nan_encoded = data_salary_encoded.isnull().sum() # the number of missing values for every column

#Putting the data together: take the numerical data from the original data.
X_num = data_salary_encoded[['Rating', 'python_yn', 'R_yn', 'spark', 'aws', 'excel']].copy()

#Take the encoded data and add to numerical data
X_final = pd.concat([X_num, job_title_encoded, job_state_encoded, type_of_ownership_encoded, industry_encoded], axis=1)

#Save the cleaned up data to a csv file in the final project Datasets directory.
X_final.to_csv('Datasets/Final Cleaned Up Salary Data.csv')

#Define y as being the "avg_salary column" from the original dataset.
y_final = data_salary_encoded[['avg_salary']].copy()

#Test train split.
X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size = 0.33, random_state = 0 )

#LINEAR REGRESSION MODEL.
from sklearn.linear_model import LinearRegression

lr = LinearRegression().fit(X_train,y_train)
lr_y_train_pred = lr.predict(X_train)
lr_y_test_pred = lr.predict(X_test)
#print score
print('lr train score %.3f, lr test score: %.3f' % (
lr.score(X_train,y_train),
lr.score(X_test, y_test)))

#POLYNOMIAL REGRESSION MODEL.
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

poly = PolynomialFeatures (degree = 2) 
X_poly = poly.fit_transform(X_final) 
X_train,X_test,y_train,y_test = train_test_split(X_poly,y_final, test_size = 0.33, random_state = 0) 

#Standard scaler (fit transform on train, fit only on test).
sc = StandardScaler() 
X_train = sc.fit_transform(X_train.astype(float))
X_test= sc.transform(X_test.astype(float))

#Fit model.
poly_lr = LinearRegression().fit(X_train,y_train)
poly_lr_y_train_pred = poly_lr.predict(X_train)
poly_lr_y_test_pred = poly_lr.predict(X_test)

#Print score.
print('poly train score %.3f, poly test score: %.3f' % (
poly_lr.score(X_train,y_train),
poly_lr.score(X_test, y_test)))

#SUPPORT VECTOR REGRESSION (SVR)
from sklearn.svm import SVR

svr = SVR(kernel='linear', C = 300) 

#Test train split.
X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size = 0.33, random_state = 0)

#Standard scaler (fit transform on train, fit only on test)
sc = StandardScaler()
X_train = sc.fit_transform(X_train.astype(float))
X_test= sc.transform(X_test.astype(float))

#Fit model.
svr = svr.fit(X_train,y_train.values.ravel()) 
svr_y_train_pred = svr.predict(X_train)
svr_y_test_pred = svr.predict(X_test)

#Print score.
print('svr train score %.3f, svr test score: %.3f' % (
svr.score(X_train,y_train),
svr.score(X_test, y_test)))

#DECISION TREE REGRESSION
from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor(random_state=0) 

#Test train split.
X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size = 0.33, random_state = 0 )

#Standard scaler (fit transform on train, fit only on test).
sc = StandardScaler()
X_train = sc.fit_transform(X_train.astype(float))
X_test= sc.transform(X_test.astype(float))

#Fit model.
dt = dt.fit(X_train,y_train.values.ravel()) 
dt_y_train_pred = dt.predict(X_train)
dt_y_test_pred = dt.predict(X_test)

#Print score.
print('dt train score %.3f, dt test score: %.3f' % (
dt.score(X_train,y_train),
dt.score(X_test, y_test)))

#RANDOM FOREST REGRESSION
from sklearn.ensemble import RandomForestRegressor

forest = RandomForestRegressor(n_estimators = 100,
criterion = 'friedman_mse',
random_state = 1,
n_jobs = -1) 

#Test train split.
X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size = 0.33, random_state = 0 )

#Standard scaler (fit transform on train, fit only on test).
sc = StandardScaler()
X_train = sc.fit_transform(X_train.astype(float))
X_test= sc.transform(X_test.astype(float))

#Fit model.
forest.fit(X_train,y_train.values.ravel()) 
forest_y_train_pred = forest.predict(X_train)
forest_y_test_pred = forest.predict(X_test)

#Print score.
print('forest train score %.3f, forest test score: %.3f' % (
forest.score(X_train,y_train),
forest.score(X_test, y_test)))

#Save predication dataframe in the final project Datasets directory for Poly Reg.
poly_lr_test_predictions = pd.DataFrame(poly_lr_y_test_pred, columns=['predictions'])
poly_lr_test_predictions['predictions'] = poly_lr_test_predictions['predictions'].apply(lambda x: "${:.2f}".format((x*1000))).to_csv('Datasets/Average Data Scientist Salary Predictions PolyReg.csv')

#Save predication dataframe in the final project Datasets directory for SVR.
svr_test_predictions = pd.DataFrame(svr_y_test_pred, columns=['predictions'])
svr_test_predictions['predictions'] = svr_test_predictions['predictions'].apply(lambda x: "${:.2f}".format((x*1000))).to_csv('Datasets/Average Data Scientist Salary Predictions SVR.csv')