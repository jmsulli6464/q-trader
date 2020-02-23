import numpy as np
import math
import pandas as pd

# df=pd.read_csv('Stocks.txt', sep=',',header=None)
# print(df.head())
# for index, row in df.iterrows():
#     row[0] = row[0].replace("\t", ",")
# print(df.head())
# df.to_csv('out.csv', index=False)

df=pd.read_csv('Stocks.csv', delimiter=',',header=None)
print(df.head())

del df[1]
df = df[~df[0].str.contains("-")]
df.to_csv('out.csv', index=False)
