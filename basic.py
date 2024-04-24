import pandas as pd

df=pd.read_csv("movies.csv")

print(df.shape)
print(df.columns)

print(df[['film','genre']])