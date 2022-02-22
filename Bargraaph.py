import pandas as pd
from matplotlib import pyplot as plot
data={'name':['vivo','oppo','redme','samsung','realme','asus','lenovo','apple','moto','lava'],
     'model':['v17 pro','f9','note11','s50','narzo','rog','lenovo k10','iphone13','fusion','zenphone'],
     'year':[2019,2018,2021,2020,2019,2021,2020,2022,2018,2017]}
df=pd.DataFrame(data)
print(df)
dataFrame=pd.DataFrame(data=data)
dataFrame.plot.bar(x='model',y='year',title='mobile model and their launched year')
plot.show(block=True)

