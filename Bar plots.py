import seaborn as sns
import matplotlib.pyplot as plt

#1 BARPLOT
product=["A","B","C","D"]
sales=[100,125,102,120]
sns.barplot(x=product,y=sales) 
plt.title("Distribution")
plt.show()

#to get predefined dataset in seaborn
sns.get_dataset_names()

# loading dataset from seaborn we use load_dataset function
import pandas as pd
df=sns.load_dataset('tips')

#day wise totalbill analysis
print(df['day'].unique())
sns.barplot(data=df,x="day",y="total_bill",errorbar=None)
plt.show()
#height of bar is the average of total bill(by default aggregation is mean)

#total of totalbill in each category
import numpy as np
print(df['day'].unique())
sns.barplot(data=df,x="day",y="total_bill",estimator=np.sum,errorbar=None)
plt.show()
