import seaborn as sns
import matplotlib.pyplot as plt

#COUNTPLOT-counts number of observations  in each category
sns.countplot(data=df,x="day")
plt.show()

#number of male and female customer in each day
sns.countplot(data=df,x="day",hue="sex")
plt.show()
