import pandas as pd

url = "data/movies_metadata.csv"

# df = DataFrame
df = pd.read_csv(url)

# print(df.head())
# df.info()
# print(df.describe())
# print(df.isnull().sum( ))

print(df[["belongs_to_collection", "homepage", "tagline"]])


# print(df.tagline)
df["tagline"].fillna("without tagline", inplace=True)   # inplace - не только изменяет данные, но и перезаписывает их
print(df.tagline)





# df["tagline"] = df["tagline"].fillna("without tagline")
# # print(df.homepage)
# df.homepage = df.homepage.fillna("no homepage")
# print(df.homepage)

