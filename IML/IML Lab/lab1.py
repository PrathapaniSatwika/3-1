import pandas as pd
data = pd.read_csv("seeds_dataset.csv")
print("Shape of the data:")
print(data.shape)
print("\nData Type:")
print(type(data))
print("\nFirst 10 rows:")
print(data.head(10))
