# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 20:45:04 2023

@author: square
"""

import pandas as pd
import matplotlib.pyplot as plt



def linear(xran,yran,xa):
    a = (yran[1]-yran[0])/(xran[1]-xran[0])
    return a*(xa - xran[0]) + yran[0]

def search_ran(xspan,yspan,xa):
    for i in range(len(xspan)-1):
        if xspan[i] >= xa and xa > xspan[i+1]:
            kx = (xspan[i],xspan[i+1])
            ky = (yspan[i],yspan[i+1])
            return kx,ky
    if xspan[0] < xa:
        kx = (xspan[0],xspan[1])
        ky = (yspan[0],yspan[1])
    else:
        kx = (xspan[-2],xspan[-1])
        ky = (yspan[-2],yspan[-1])
    return kx,ky

def fit1d(xt,yt,xa):
    kx,ky = search_ran(xt,yt,xa)
    y = linear(kx,ky,xa)
    return y




df = pd.read_csv("proc-data.txt",sep="\t")

fig,ax = plt.subplots()
df = df.iloc[3:]
x = df["AD"]
y = df["distance"]

SKIP = 4
xt = list(df["AD"].iloc[::SKIP])
yt = list(df["distance"].iloc[::SKIP])
# yt = pd.Series([10000]*xt.shape[0])

print(xt)
print(yt)

ax.scatter(x,y)
ax.plot(xt,yt,c='r')

xa = 40000
ax.scatter(xa,fit1d(xt,yt,xa),s=90)
print(fit1d(xt,yt,xa))


