
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url)




print(df.head(2))
#print(df.tail(2))
#print(df.dtypes)
#print(df.describe)
#print(df.dropna())
#print(df.dropna(subset=["price"],axis=0,inplace=True))#0 entire row 1 entire column
#mean=df["normalized-losses"].mean()
#print(df["normalized-losses"].replace(pd.nan,mean))#missing value, new value
