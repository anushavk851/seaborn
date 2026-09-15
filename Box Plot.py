import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=df,x="total_bill")
plt.show()

#daywise boxplot
sns.boxplot(data=df,x="total_bill",y="day",hue="sex")
plt.show()
