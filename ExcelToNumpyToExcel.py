import numpy as np
import pandas as pd
import time

myPath = 'TwoTimes3x3Matricies.xlsx'
maxRange = 10000


df1 = pd.read_excel(myPath, header=None)
df2 = pd.read_excel(myPath, 1, header=None)
np1 = df1.to_numpy()
np2 = df2.to_numpy()


tic1 = time.time()
for i in range(1, maxRange):
    df3 = np.dot(df1,df2)
toc1 = time.time()

tic2 = time.time()
for i in range(1, maxRange):
    np3 = np.dot(np1,np2)
toc2 = time.time()

print("df3 ", df3)
print("np3 ", np3)
print()
print("time for df3: ", str(toc1-tic1))
print("time for np3: ", str(toc2-tic2))

df4 = pd.DataFrame.from_records(df3)
df4.to_excel("result_"+myPath, sheet_name="Alex")