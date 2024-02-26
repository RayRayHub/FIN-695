import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.utils import plot_model

tf.random.set_seed(0)
X = np.array([1,2,3,4,5,6,7,8,9,10], dtype=float)
y = np.array([5,7,9,11,13,15,17,19,21,23], dtype=float)

model = keras.models.Sequential()
model.add(keras.layers.Dense(1,input_shape=[1]))
model.compile(loss='mean_squared_error',  
              optimizer=keras.optimizers.Adam(lr=0.1))
# print model summary
print(model.summary())
# Save the plotted model
#plot_model(model, to_file="first_nn.png",show_shapes=True)
# Print out the initial weight and bias
w0, bias0 = model.layers[-1].get_weights()
print("the initial weight is", w0)
print("the initial bias is", bias0)
# Train the model
model.fit(X, y, epochs=1000, verbose=0)
# Use the model to predicdt
X_test = [[11], [12], [13], [14], [15]]
pred = model.predict(X_test)
print("the model predictions are\n", pred)
# Print out final weight and bias
w1, bias1 = model.layers[-1].get_weights()
print("the final weight is", w1)
print("the final bias is", bias1)
# Use final weight and bias to calcualte predictions
manual_pred = bias1 + w1 * X_test
print("the manually calcualted predictions are\n", manual_pred)
