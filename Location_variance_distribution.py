import statistics
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = 'clean_russia_losses_equipment.csv'
clean_data = pd.read_csv(data)
#add a column to the data that shows the day of the week for each date, in column 2
clean_data['date'] = pd.to_datetime(clean_data['date'])
clean_data['day of week'] = clean_data['date'].dt.day_name()
#add a column to the data that shows the month for each date, in column 3
clean_data['month'] = clean_data['date'].dt.month_name()
print(clean_data.head())



#calculating arithmetic mean for each column except the first one
mean = statistics.mean(clean_data['APC'])
print('APC arithmetic mean:', mean)

#calculating geometric mean for the APC column
#first, remove the zeros
apc = clean_data['APC']
apc = [x for x in apc if x != 0]
geometric_mean = statistics.geometric_mean(apc)
print('APC geometric mean:', geometric_mean)

#Calculating the harmonic mean for the APC column
harmonic_mean = statistics.harmonic_mean(apc)
print('APC harmonic mean:', harmonic_mean)

#Calculating the mode for the APC column
mode = statistics.mode(apc)
print('APC mode:', mode)

#Calculating the median for the APC column
median = statistics.median(apc)
print('APC median:', median)

#Calculate the variance for the APC column
variance = statistics.variance(clean_data['APC'])
print('APC variance:', variance)

#Calculating the standard deviation for the APC column
standard_deviation = statistics.stdev(apc)
print('APC standard deviation:', standard_deviation)

#plotting the location variance distribution
plt.hist(apc, bins=10, edgecolor='black')
plt.title('APC losses')
plt.xlabel('APC')
plt.ylabel('count')
plt.show()


#plotting the violin plot for the distribution of losses
sns.violinplot(data=clean_data['APC'],orient='h')
plt.title('Losses distribution')
plt.show()


#plotting the box plot for the distribution of losses with strip plot
sns.boxplot(data=clean_data['APC'],orient='h',  whis=1.5)
plt.title('Losses distribution')
plt.show()


#plotting a graph with vertical lines to show the mean, median and mode of the APC losses
sns.kdeplot(apc, shade=True)
plt.axvline(mean, color='red', label='mean')
plt.axvline(median, color='yellow', label='median')
plt.axvline(geometric_mean, color='green', label='geometric mean')
plt.axvline(harmonic_mean, color='blue', label='harmonic mean')
plt.axvline(mode, color='black', label='mode')
plt.title('APC losses central tendency')
plt.xlabel('APC')
plt.ylabel('density')
plt.legend()
plt.show()

#calculating correlation between the losses and aircraft losses
correlation = clean_data['APC'].corr(clean_data['aircraft'])
print('Correlation between APC and aircraft losses:', correlation)

#calculating the covariance between the losses and aircraft losses
covariance = clean_data['APC'].cov(clean_data['aircraft'])
print('Covariance between APC and aircraft losses:', covariance)

plt.hist(clean_data['aircraft'], bins=10, edgecolor='black')
plt.title('Aircraft losses')
plt.xlabel('aircraft')
plt.ylabel('count')
plt.show()



#plotting the scatter plot for the losses and aircraft losses
plt.scatter(clean_data['APC'], clean_data['aircraft'])
plt.title('APC losses vs aircraft losses')
plt.xlabel('APC')
plt.ylabel('aircraft')
plt.show()

#creatng a figure with 2 subplots to show the distribution of losses and aircraft losses
fig, ax = plt.subplots(1,2)
ax[0].hist(clean_data['APC'], bins=30, edgecolor='black')
ax[0].set_title('APC losses')
ax[0].set_xlabel('APC')
ax[0].set_ylabel('count')
ax[1].hist(clean_data['aircraft'], bins=30, edgecolor='black')
ax[1].set_title('Aircraft losses')
ax[1].set_xlabel('aircraft')
ax[1].set_ylabel('count')
plt.show()

#plotting heatmap to show the correlation between the APC losses and aircraft losses
correlation_matrix = clean_data.corr()
sns.heatmap(correlation_matrix)
plt.title('Correlation matrix')
plt.show()

#plotting distribution of losses with mean and different standard deviation intervals
sns.kdeplot(apc, shade=True)
plt.axvline(mean, color='red', label='mean')
plt.axvline(mean+standard_deviation, color='yellow', label='+1 std')
plt.axvline(mean-standard_deviation, color='yellow', label='-1 std')
plt.axvline(mean+2*standard_deviation, color='green', label='+2 std')
plt.axvline(mean-2*standard_deviation, color='green', label='-2 std')
plt.axvline(mean+3*standard_deviation, color='blue', label='+3 std')
plt.axvline(mean-3*standard_deviation, color='blue', label='-3 std')
plt.title('APC losses distribution with mean and standard deviation intervals')
plt.xlabel('APC')
plt.ylabel('density')
#plot legend outside the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

#plotting sum of APC losses by day of the week and moth in a figure with 2 subplots with month and day of week ordered to start from January and Monday respectively
order_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
order_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
fig, ax = plt.subplots(1,3,gridspec_kw={'width_ratios': [2, 2, 3]})
#title for the figure
fig.suptitle('Losses vs time')
sns.barplot(x='day of week', y='APC', data=clean_data, estimator=sum, ci=None, order=order_day, ax=ax[0])
ax[0].set_title('losses by day of the week')
#rotate the x-axis labels
ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation=90)
ax[0].set_xlabel('day of week')
ax[0].set_ylabel('sum of APC losses')
sns.barplot(x='month', y='APC', data=clean_data, estimator=sum, ci=None, order=order_month, ax=ax[2])
ax[2].set_title('losses by month')
#rotate the x-axis labels
ax[2].set_xticklabels(ax[2].get_xticklabels(), rotation=90)
ax[2].set_xlabel('month')
ax[2].set_ylabel('sum of APC losses')
#ploting losses in January per day of the week
january = clean_data[clean_data['month']=='January']
sns.barplot(x='day of week', y='APC', data=january, estimator=sum, ci=None, order=order_day, ax=ax[1])
ax[1].set_title('Jan losses')
ax[1].set_ylabel('sum of APC losses')
#rotate the x-axis labels
ax[1].set_xticklabels(ax[1].get_xticklabels(), rotation=90)
plt.tight_layout()
plt.show()
 
#piechart to show the distribution of losses by month
losses_by_month = clean_data.groupby('month')['APC'].sum()
losses_by_month = losses_by_month.reindex(order_month)
plt.pie(losses_by_month, labels=losses_by_month.index, autopct='%1.1f%%')
plt.title('APC losses by month')
plt.show()

#scatter figure with suplots to show the distribution of losses by month, colour min values per month red and max in blue. 1 with ordered by other and other without
fig, ax = plt.subplots()
scatter = ax.scatter(clean_data['month'], clean_data['APC'], c=clean_data['APC'], cmap='coolwarm')
ax.set_xlabel('month')
ax.set_ylabel('APC')
ax.set_title('Min & Max losses by month')
#rotate the x-axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
#color bar
cbar = plt.colorbar(scatter)
cbar.set_label('APC')
plt.show()

