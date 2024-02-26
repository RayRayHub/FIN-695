import pandas as pd

data = pd.read_csv("insurance.csv")
print(data.head(10))

#check how many values are missing (NaN)
count_nan = data.isnull().sum()
print(count_nan[count_nan > 0])

#fill in the missing values
data.bmi.fillna(data.bmi.mean(), inplace = True)
count_nan_after_fill = data.isnull().sum()
print(count_nan_after_fill[count_nan_after_fill > 0])

#throw out any observations with missing values
data1 = data.dropna()

import matplotlib.pyplot as plt
import seaborn as sns

figure, ax = plt.subplots(4,2, figsize=(12,24))
#See the distrubution of the data
sns.distplot(data['charges'],ax= ax[0,0])
sns.distplot(data['age'],ax=ax[0,1])
sns.distplot(data['bmi'],ax= ax[1,0])
sns.distplot(data['children'],ax= ax[1,1])
sns.countplot(x=data['sex'],ax=ax[2,0])
sns.countplot(x=data['smoker'],ax= ax[2,1])
sns.countplot(x=data['region'],ax= ax[3,0])

sns.pairplot(data)

sns.lmplot(x="age", y="charges", hue="smoker", data=data, palette="muted", height=7)

corr=data.corr()
sns.heatmap(corr, annot=True)

data.replace(("yes", "no"),(1,0),inplace=True)
data.replace(("female", "male"),(1,0),inplace=True)

region = data.region
encoded_region = pd.get_dummies(region)

#combine dataframes into one using concat
final_data=pd.concat([data,encoded_region], axis=1)

#label(target) LH variable insurance premium 
y_final = final_data[["charges"]]
X_final = final_data.drop(["region", "charges"], axis=1)

#train test
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X_final, y_final, test_size=0.33, random_state=0)

# feature scaling
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train,)
X_test=scaler.transform(X_test)
pd.DataFrame(X_train).describe()

import numpy as np
X_train = np.array(X_train).reshape(-1,9)
y_train = np.array(y_train).reshape(-1,1)
X_test = np.array(X_test).reshape(-1,9)
y_test = np.array(y_test).reshape(-1,1)

import tensorflow as tf
dnn=tf.keras.Sequential()
dnn.add(tf.keras.layers.Dense(128, input_shape=[9], activation="relu"))
dnn.add(tf.keras.layers.Dense(64, activation="relu"))
dnn.add(tf.keras.layers.Dense(32, activation="relu"))
dnn.add(tf.keras.layers.Dense(1, activation="relu"))

dnn.compile(optimizer="adam", loss="mean_squared_error")
dnn.fit(X_train, y_train, epochs=50)

y_train_pred=dnn.predict(X_train)
y_test_pred=dnn.predict(X_test)

#average performance is R-squared
from sklearn.metrics import r2_score

#y_test is the actual value
#y_test_pred is the preditions
r2 = r2_score(y_test, y_test_pred)