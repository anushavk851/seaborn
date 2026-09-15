import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(data=df,x="total_bill",y="tip")
plt.show()

df1=sns.load_dataset('flights')
df1
sns.lineplot(data=df1,x="year",y="passengers")
plt.show()
