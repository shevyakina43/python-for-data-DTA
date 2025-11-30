import pandas as pd

url = "data/movies_metadata.csv"

# df()
df = pd.read_csv(url)

# print(df.head())
# df.info()
# print(df.describe())
# print(df.isnull().sum( ))

print(df[["belongs_to_collection", "homepage", "tagline"]])

df["tagline"]
print(df.tagline)