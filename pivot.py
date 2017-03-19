#!/usr/bin/python2.7

import pandas as pd
import numpy as np

df = pd.read_excel("sales-funnel.xlsx")
df.head()
df["Status"] = df["Status"].astype("category")
df["Status"].cat.set_categories(["won","pending","presented","declined"],inplace=True)
#print(df["Status"])

#pd.pivot_table(df,index=["Name","Rep","Manager"])
#pd.pivot_table(df,index=["Manager","Rep"],values=["Price"])
piv=pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],aggfunc=np.sum)
print(piv)