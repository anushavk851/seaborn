import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(data=df,x="total_bill",y="tip")
plt.show()
