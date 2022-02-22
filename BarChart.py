import pandas as pd
from matplotlib import pyplot as pt
data={'sub':['PHP','DS'],'marks':[90,80]}
df=pd.DataFrame(data)
df.plot(kind="bar")
pt.show()
