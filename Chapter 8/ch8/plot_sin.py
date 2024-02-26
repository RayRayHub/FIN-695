import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,1000) 
y = np.square(x)
y2= np.cos(x)

plt.plot(x, y, c="blue", linestyle="^^")
plt.plot(x, y2, c="red")
plt.xlabel('x')
plt.ylabel('y')
plt.title('function sin(x)')
plt.show() 

np.square(x)