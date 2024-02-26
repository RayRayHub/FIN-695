import pandas as pd

df = pd.read_csv("presidents.csv")

dfNameIndex = pd.read_csv("presidents.csv", index_col=("name"))

print(dfNameIndex.shape)
print(dfNameIndex.shape[0])
print(dfNameIndex.size)

print(dfNameIndex.head)
print(dfNameIndex.tail(n=8))
print(dfNameIndex.describe())

print("the median height and age of the 45 presidents are", dfNameIndex[['height','age']].median())
print(dfNameIndex[['height','age']].min())

import numpy as np
df=pd.read_csv("presidents.csv")
df.plot(kind="scatter", x="age", y="height").
df.height.plot(kind="hist", bins=15)


import numpy as np
arr = np.array([[ 1, 2, 3], [2, 4, 6]])
arr[:,0]*3
arr[0] * 3
arr[0,:]*3