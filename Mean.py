import statistics as st
import numpy as np
data=[5,9,25,12,4,30,5,20,12,5]
print("Arithmetic mean=",end=" ")
print(st.mean(data))

print("Median=",end=" ")
print(st.median(data))

print("mode=",end=" ")
print(st.mode(data))

print("standard deviation=",end=" ")
print(np.std(data))

data=np.array([10,20,30,40,50,60,70,80,90,100,110,120])
q=st.quantiles(data)
print("quantiles=",q)

