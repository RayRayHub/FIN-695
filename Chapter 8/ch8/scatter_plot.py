import matplotlib.pyplot as plt
import pandas as pd

presidents_df = pd.read_csv('presidents.csv', index_col='name')

plt.scatter(presidents_df['height'], presidents_df['age'])
plt.show() 
