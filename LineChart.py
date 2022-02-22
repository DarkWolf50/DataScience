import pandas as pd
import matplotlib.pyplot as plot
data={'Month':['jun','july','aug','sep'],
      'AvgTemp':[35,37,40,30],
      'Rainfall':['light Rain','Heavy rain','extremly rainstrom','normal rainfall']}
df=pd.DataFrame(data)
print(df)
plot.plot(df['Rainfall'],df['AvgTemp'],'-')
plot.show()

