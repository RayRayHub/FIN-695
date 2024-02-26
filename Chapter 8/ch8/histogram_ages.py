#import matplotlib.pyplot as plt
import pandas as pd

presidents_df = pd.read_csv('presidents.csv', index_col='name')
presidents_df.age.plot(kind='hist',bins=10)
# plt.show()
# plt.hist(presidents_df['ages'], bins=10)
# plt.show()