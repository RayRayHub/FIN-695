# Put file presidents.csv in the same folder as this script 
import pandas as pd
presidents_df = pd.read_csv('presidents.csv', index_col='name')

print(presidents_df.columns)
print(presidents_df['height'])
print(presidents_df['height'].shape)
print(presidents_df[['height','age']].head(n=3))
print(presidents_df.age.mean())

