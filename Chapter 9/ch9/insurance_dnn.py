from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import r2_score
import tensorflow as tf

data = pd.read_csv("insurance.csv")
data['bmi'].fillna(data['bmi'].mean(), inplace = True)


sex = data.iloc[:,1:2].values
smoker = data.iloc[:,4:5].values

le = LabelEncoder()
sex[:,0] = le.fit_transform(sex[:,0])
sex = pd.DataFrame(sex)
sex.columns = ['sex']
le_sex_mapping = dict(zip(le.classes_, le.transform(le.classes_)))


le = LabelEncoder()
smoker[:,0] = le.fit_transform(smoker[:,0])
smoker = pd.DataFrame(smoker)
smoker.columns = ['smoker']
le_smoker_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
print("Sklearn label encoder results for smoker:")  
print(le_smoker_mapping)
print(smoker[:10])

region = data.iloc[:,5:6].values #ndarray
ohe = OneHotEncoder() 
region = ohe.fit_transform(region).toarray()
region = pd.DataFrame(region)
region.columns = ['northeast', 'northwest', 'southeast', 'southwest']



X_num = data[['age', 'bmi', 'children']].copy()

X_final = pd.concat([X_num, region, sex, smoker], axis = 1)

y_final = data[['charges']].copy()

# Split
X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size = 0.33, random_state = 0 )
# standarize variables
s_scaler = StandardScaler()
X_train = s_scaler.fit_transform(X_train.astype(np.float))
X_test= s_scaler.transform(X_test.astype(np.float))


# DNN method

X_train = np.array(X_train).reshape((-1,9))
print(X_train.shape)

y_train = np.array(y_train).reshape((-1,1))
print(y_train.shape)

X_test = np.array(X_test).reshape((-1,9))
print(X_test.shape)

y_test = np.array(y_test).reshape((-1,1))

print(y_test.shape)


dnn = tf.keras.Sequential()
dnn.add(tf.keras.layers.Dense(128,input_shape=[9],activation="relu"))
dnn.add(tf.keras.layers.Dense(64,activation="relu"))
dnn.add(tf.keras.layers.Dense(32,activation="relu"))
dnn.add(tf.keras.layers.Dense(1, activation='relu'))

dnn.compile(optimizer="adam", loss="mean_squared_error")

dnn.fit(X_train, y_train,verbose=1, epochs=50)

y_train_pred_dnn=dnn.predict(X_train)

y_test_pred_dnn=dnn.predict(X_test)

y_true=np.array(y_test)
dif=y_true-y_test_pred_dnn

ss_total=np.square(y_true-np.mean(y_true))
ss_res = np.square(dif)


rsq = 1-sum(ss_res)/sum(ss_total)
print("R-squared for testing data based on 1-sum(ss_res)/sum(ss_total) is", rsq)

print("R-squared for training data is", r2_score(y_train, y_train_pred_dnn))
print("R-squared for testing data is", r2_score(y_true, y_test_pred_dnn))
















