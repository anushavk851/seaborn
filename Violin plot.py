import seaborn as sns
import matplotlib.pyplot as plt

sns.violinplot(data=df,x="day",y="total_bill")
plt.show()

#combined version of boxplot,kde and histogram
