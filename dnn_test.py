import pandas as pd


df = pd.DataFrame([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]], \
    columns=["col1", "col2", "col3", "col4"])
print(df)


print(df.mean(axis=1))