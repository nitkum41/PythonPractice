import pandas as pd
import numpy as np

series = {
    'name': ['A', 'B', 'C', 'D'],
    'age': [10, 20, 30, 40],
    'loc': ['XX', 'YY', 'ZZ', 'WW']
}

# df = pd.DataFrame(series)

arr = np.array([[1, 2, 3], [-1, -2, -3], [0, 1, 0]])
# print(arr[1][2])
df = pd.DataFrame(arr, columns=['first', 'second', 'third'])
#
# print(df.columns)
# val=[]
# for i in range(len(df)):
#     val.append(df['first'][i] + df['second'][i] + df['third'][i])
#
# df.insert(3,'fourth',val)
# x=df.pop('fourth')
# y=df.pop('third')
# print(x)
# df.insert(0,'fo',x)
# # df.insert(1,'th',y)
# print(df.head())
# df=df.first
# df=df.values.reshape(-1,1)
print(df.head())