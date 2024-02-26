import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000) 
plt.plot(x, np.sin(x), color='blue', label="sin function")
plt.plot(x, np.cos(x), color='green', linestyle ='--', label="cos function")
plt.legend()
plt.show() 
