import pandas as pd
from matplotlib import pyplot as plot
data={'name':['rahul','aman','sham','gopal','aniket','tushar','virat','rohit','raju','vaibhu'],
     'age':[50,44,55,22,44,88,60,30,25,66],
     'addres':['nagar','pune','nashik','shrirampur','mumbai','rahta','rahuri','raygad','aurangabad','jalna']}
df=pd.DataFrame(data)
print(df)
dataFrame=pd.DataFrame(data=data)
dataFrame.plot.bar(x='name',y='age',title='customer name and their age')
plot.show(block=True)

