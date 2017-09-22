from pandas import DataFrame, Series

df = DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'f']})



print(df)

print(df.isin([1]))