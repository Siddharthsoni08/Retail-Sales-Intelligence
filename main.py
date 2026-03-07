import pandas as pd

df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

print(df.head())

# Dataset size 
print("Dataset Shape:", df.shape)

#column Names
print("\nColumns:")

#dataset info
print("\nDataset Info:")
print(df.info())

#convert date columns 
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nDate conversion done")

print(df.dtypes)