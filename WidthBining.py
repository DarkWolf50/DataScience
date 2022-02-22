import pandas as pd
import numpy as np
from matplotlib import pyplot as plot
data={'item':['shirt','sweater','bodywarmer','bodynapkin'],
     'price':[300,500,1100,160]}
df=pd.DataFrame(data)
print("original")
print("-----------------------")
print(df)
m1=min(df["price"])
m2=max(df["price"])
bins=np.linspace(m1,m2,4)
name=["low","medium","high"]
df["price_bin"]=pd.cut(df["price"],bins,labels=name,include_lowest=True)
print("\nBINING DATA")
print("---------------------------")
print(df)
