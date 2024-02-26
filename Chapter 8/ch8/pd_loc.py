# Put file presidents.csv in the same folder as this script 
import pandas as pd
presidents_df = pd.read_csv('presidents.csv', index_col='name')

print(presidents_df.loc['Abraham Lincoln'])
print(type(presidents_df.loc['Abraham Lincoln']))
print(presidents_df.loc['Abraham Lincoln'].shape)

print(presidents_df.loc['Abraham Lincoln':'Ulysses S. Grant'])

print(presidents_df.iloc[25])


#print(presidents_df['party'])
#print(presidents_df['age'].min())
#print(presidents_df['age'].argmin())
#print(presidents_df[25:26])
