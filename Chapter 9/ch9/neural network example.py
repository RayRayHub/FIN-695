import numpy as np
import tensorflow as tf
from tensorflow import keras
X = np.array([1,2,3,4,5,6,7,8,9,10], dtype=float)
y = np.array([5,7,9,11,13,15,17,19,21,23], dtype=float)
#neural network
model = keras.models.Sequential()
model.add(keras.layers.Dense(1,input_shape=[1]))
model.compile(loss='mean_squared_error',
optimizer=keras.optimizers.Adam(lr=0.1))
model.fit(X, y, epochs=1000)
pred = model.predict([[11],
[12],
[13],
[14],
[15]])
print(pred)