#Heatmap
corr=df.corr(numeric_only=True) #correlation
sns.heatmap(corr)
plt.show()

#graphical representation of data using different colors.useful for understanding values in a matrix such as correlation between columns in a dataset
corr=df.corr(numeric_only=True) 
sns.heatmap(corr,annot=True)
plt.show()
