import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Zadanie 1
print("---------")
print("1.1, 1.2 reading file and setting seed")
banctuptcy = pd.read_csv("bankruptcy.csv")
np.random.seed(1234)


print("---------")
print("1.3, 1.4 setting 2 random cells in numeric colums as empty cells")
unique_row_idx = random.sample(list(banctuptcy.index), banctuptcy.shape[1] - 1)
for row, col in zip(unique_row_idx, banctuptcy.columns[2:7]):
    banctuptcy.at[row, col] = None

unique_row_idx = random.sample(list(banctuptcy.index), banctuptcy.shape[1] - 1)
for row, col in zip(unique_row_idx, banctuptcy.columns[2:7]):
    banctuptcy.at[row, col] = None

print("---------")
print("1.5 basic descriptive statistics")

print("Na")
print(banctuptcy.isna().sum())
print("Mean")
print(banctuptcy.mean( numeric_only=True))
print("Std")
print(banctuptcy.std( numeric_only=True))
print("Max")
print(banctuptcy.max( numeric_only=True))
print("Min")
print(banctuptcy.min( numeric_only=True))

print(banctuptcy.head())
print("---------")
print("Zadanie 1.6")
banctuptcy = banctuptcy.fillna(banctuptcy.mean())
print(banctuptcy.isna().sum())


print("---------")
print("1.7 Basic descriptive statistics")
print(banctuptcy.isna().sum())
print(banctuptcy.mean(numeric_only=True))
print(banctuptcy.std(numeric_only=True))
print(banctuptcy.max(numeric_only=True))
print(banctuptcy.min(numeric_only=True))

print("---------")
print("1.8 saving to a file")
banctuptcy.to_csv('banctuptcysales_uzupelnione.csv')
