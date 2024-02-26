import matplotlib.pyplot as plt
import pandas as pd
presidents_df = pd.read_csv('presidents.csv', index_col='name')
party_cnt = presidents_df['party'].value_counts()
plt.style.use('ggplot')
party_cnt.plot(kind ='bar')
plt.show() 
