import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Zadanie 1
vg = pd.read_csv("vgsales.csv")
np.random.seed(1234)

unique_row_idx = random.sample(list(vg.index), vg.shape[1] - 1)
for row, col in zip(unique_row_idx, vg.columns[6:11]):
    vg.at[row, col] = None

unique_row_idx = random.sample(list(vg.index), vg.shape[1] - 1)
for row, col in zip(unique_row_idx, vg.columns[6:11]):
    vg.at[row, col] = None

print("IsNa")
print(vg.isna().sum())

print(vg.mean(axis=0))
print(vg.std(axis=0))
print(vg.max(axis=0))
print(vg.min(axis=0))


print(vg.isna().sum())


print("hej")


print(vg.head())

for x in range(0,16599):
    for x in range(0,11):
        if vg.loc[x,y] == None:
            vg.loc[x,y] = 1

print(vg)
print(vg.isna().sum())

print("hej")
#vg._set_value(2,vg.columns[0],20)
#print(vg.loc[1,2])

