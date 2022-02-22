import pandas as pd
data={'name':['Akshay','Rahul','Aman','Ganesh','Sagar','Vinod','Danny','Sham','Nikhil','Sarthak'],
     'age':[20,21,22,22,22,21,21,20,20,22],
     'Percentage':[80,85,66,76,88,90,99,55,84,50]}
df=pd.DataFrame(data)
print(df)
mean_df=df.mean()
print(mean_df)
