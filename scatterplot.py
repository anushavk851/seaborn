import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=df,x="total_bill",y="tip")
plt.show()

#gender analysis to ad different color to categorical column.
#hues= used to represent amother categorical values using different colors
sns.scatterplot(data=df,x="total_bill",y="tip",hue="sex")
plt.show()

#hue-used to represent another categorical values using different colors
sns.scatterplot(data=df,x="total_bill",y="tip",hue="smoker")
plt.show()

#style-gives different marker points to each category
sns.scatterplot(data=df,x="total_bill",y="tip",hue="sex",style="smoker")
plt.show()

#size-adjusts marker size
sns.scatterplot(data=df,x="total_bill",y="tip",hue="sex",style="smoker",size='size') #number of people=size
plt.show()

