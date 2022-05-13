import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Zadanie 1
print("---------")
print("Zadanie 1.1,1.2")
vg = pd.read_csv("vgsales.csv")
np.random.seed(1234)

print("---------")
print("Zadanie 1.3,1.4")
unique_row_idx = random.sample(list(vg.index), vg.shape[1] - 1)
for row, col in zip(unique_row_idx, vg.columns[6:11]):
    vg.at[row, col] = None

unique_row_idx = random.sample(list(vg.index), vg.shape[1] - 1)
for row, col in zip(unique_row_idx, vg.columns[6:11]):
    vg.at[row, col] = None

print("---------")
print("Zadanie 1.5")

print("IsNa")
print(vg.isna().sum())
print(vg.mean(axis=0))
print(vg.std(axis=0))
print(vg.max(axis=0))
print(vg.min(axis=0))

print(vg.head())
print("---------")
print("Zadanie 1.6")
#for x in range(0,16599):
#    for y in range(0,11):
#        if vg.loc[x,y]:
#            vg.loc[x,y] = 1

#print(vg.loc[1,1])
#vg._set_value(2,vg.columns[0],20)
#print(vg.loc[1,2])

print("---------")
print("Zadanie 1.7")


print("---------")
print("Zadanie 1.8")
