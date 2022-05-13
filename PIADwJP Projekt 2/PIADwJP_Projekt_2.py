import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Zadanie 1
print("---------")
print("1.1, 1.2 reading file and setting seed")
vg = pd.read_csv("vgsales.csv")
np.random.seed(1234)


print("---------")
print("1.3, 1.4 setting 2 random cells in numeric colums as empty cells")
unique_row_idx = random.sample(list(vg.index), vg.shape[1] - 1)
for row, col in zip(unique_row_idx, vg.columns[6:11]):
    vg.at[row, col] = None

unique_row_idx = random.sample(list(vg.index), vg.shape[1] - 1)
for row, col in zip(unique_row_idx, vg.columns[6:11]):
    vg.at[row, col] = None

print("---------")
print("1.5 basic descriptive statistics")

print(vg.isna().sum())
print(vg.mean( numeric_only=True))
print(vg.std( numeric_only=True))
print(vg.max( numeric_only=True))
print(vg.min( numeric_only=True))

print(vg.head())
print("---------")
print("Zadanie 1.6")
vg = vg.fillna(vg.mean())
print(vg.isna().sum())
#for x in range(0,11):
    #for y in range(0,16599):
        #if vg[x,y] == None:
            #vg.loc[x,y] = 1


#print(vg.loc[1,1])
#vg._set_value(2,vg.columns[0],20)
#print(vg.loc[1,2])

print("---------")
print("1.7 Basic descriptive statistics")
print(vg.isna().sum())
print(vg.mean(numeric_only=True))
print(vg.std(numeric_only=True))
print(vg.max(numeric_only=True))
print(vg.min(numeric_only=True))

print("---------")
print("1.8 saving to a file")
vg.to_csv('vgsales_uzupelnione.csv')
