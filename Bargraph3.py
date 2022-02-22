import pandas as pd
from matplotlib import pyplot as plot
data={'name':['amol','saurabh','nikhil','swapnil','kunal','prashant','kojar','shubham','mayur','harshal'],
     'age':[25,23,24,25,22,23,26,27,27,25],
     'salary':[10000,20000,25000,18000,20000,30000,40000,50000,25000,22000]}
df=pd.DataFrame(data)
print(df)
dataFrame=pd.DataFrame(data=data)
dataFrame.plot.bar(x='name',y='salary',title='employee and their salary graph');
plot.show(block=True);
