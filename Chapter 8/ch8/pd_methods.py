# Put file presidents.csv in the same folder as this script 
import pandas as pd
presidents_df = pd.read_csv('presidents.csv', index_col='name')

print(presidents_df.min())
print(presidents_df.max())
print(presidents_df.mean())
print("when starting office, the average U.S president age is", presidents_df['age'].mean())

