import seaborn as sns
import matplotlib.pyplot as plt

#KERNEL DENSITY ESTIMATE(KDE)--Represents destribution of numerical data as smooth curve
# instead of bar if we need smooth curve in histogram we use kde
sns.kdeplot(data=df,x="total_bill")
plt.show()

#compaining histogram and kde
sns.histplot(data=df,x="total_bill",bins=10,kde=True)
plt.show()
