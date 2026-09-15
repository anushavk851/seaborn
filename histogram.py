import seaborn as sns
import matplotlib.pyplot as plt

#distribution of total bill we use histogram
sns.histplot(data=df,x="total_bill",bins=10)
plt.show()
