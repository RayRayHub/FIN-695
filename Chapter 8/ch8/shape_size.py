# Put file presidents.csv in the same folder as this script 
import pandas as pd
presidents_df = pd.read_csv('presidents.csv', index_col='name')

print(presidents_df.shape)
print(presidents_df.shape[0])
print(presidents_df.size)
print(presidents_df.tail(n=3))
print(presidents_df.info())

print(presidents_df["height"].shape)
print("the median height and age of the 45 presidents are", presidents_df[['height','age']].median())
print(presidents_df['age'].min())

print(presidents_df[45-6:])
print(presidents_df.tail(6))

print(presidents_df.shape[0])
#print(presidents_df.nrow())
print(presidents_df.shape[1])








