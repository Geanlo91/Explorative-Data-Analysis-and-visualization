import statistics
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = 'clean_russia_losses_equipment.csv'
clean_data = pd.read_csv(data)
print(clean_data.head())

#add a column to the data that shows the day of the week for each date, in column 2
clean_data['date'] = pd.to_datetime(clean_data['date'])
clean_data['day of week'] = clean_data['date'].dt.day_name()


#calculate arithmetic mean for each column except the first one
mean = statistics.mean(clean_data['APC'])
print('APC arithmetic mean:', mean)

#calcculate geometric mean for the APC column
#first, remove the zeros
apc = clean_data['APC']
apc = [x for x in apc if x != 0]
geometric_mean = statistics.geometric_mean(apc)
print('APC geometric mean:', geometric_mean)

#Calculate the harmonic mean for the APC column
harmonic_mean = statistics.harmonic_mean(apc)
print('APC harmonic mean:', harmonic_mean)

#Calculate the mode for the APC column
mode = statistics.mode(apc)
print('APC mode:', mode)

#Calculate the median for the APC column
median = statistics.median(apc)
print('APC median:', median)

#Calculate the variance for the APC column
variance = statistics.variance(clean_data['APC'])
print('APC variance:', variance)

#Calculate the standard deviation for the APC column
standard_deviation = statistics.stdev(apc)
print('APC standard deviation:', standard_deviation)

#plot the location variance distribution
plt.hist(apc, bins=10, edgecolor='black')
plt.title('APC losses')
plt.xlabel('APC')
plt.ylabel('count')
plt.show()
#The plot shows that the distribution of APC losses is skewed to the right
#This means that the majority of the losses are small and a few are large
#This is consistent with the high variance and standard deviation values


#plot the violin plot for the distribution of losses
sns.violinplot(data=clean_data['APC'],orient='h')
plt.title('Losses distribution')
plt.show()


#plot the box plot for the distribution of losses with strip plot
sns.boxplot(data=clean_data['APC'],orient='h',  whis=1.5)
plt.title('Losses distribution')
plt.show()
 

#plot the sum of losses for each day of the week
day_of_week = clean_data['day of week']
losses = clean_data['APC']
day_loss = dict(zip(day_of_week, losses))
day_loss = Counter(day_loss)
print(day_loss)
plt.bar(day_loss.keys(), day_loss.values())
plt.title('APC losses by day of the week')
plt.xlabel('Day of the week')
plt.ylabel('APC')
plt.show()

#plot a graph with vertical lines to show the mean, median and mode of the APC losses
sns.kdeplot(apc, shade=True)
plt.axvline(mean, color='red', label='mean')
plt.axvline(median, color='yellow', label='median')
plt.axvline(geometric_mean, color='green', label='geometric mean')
plt.axvline(harmonic_mean, color='blue', label='harmonic mean')
plt.title('APC losses central tendency')
plt.xlabel('APC')
plt.ylabel('count')
plt.legend()
plt.show()

sns.kdeplot(apc, shade=True)
plt.axvline(mode, color='black', label='mode')
plt.title('APC losses central tendency')
plt.xlabel('APC')
plt.ylabel('count')
plt.legend()
plt.show()

#calculate correlation between the losses and aircraft losses
correlation = clean_data['APC'].corr(clean_data['aircraft'])
print('Correlation between APC and aircraft losses:', correlation)

#calculate the covariance between the losses and aircraft losses
covariance = clean_data['APC'].cov(clean_data['aircraft'])
print('Covariance between APC and aircraft losses:', covariance)

plt.hist(clean_data['aircraft'], bins=10, edgecolor='black')
plt.title('Aircraft losses')
plt.xlabel('aircraft')
plt.ylabel('count')
plt.show()



#plot the scatter plot for the losses and aircraft losses
plt.scatter(clean_data['APC'], clean_data['aircraft'])
plt.title('APC losses vs aircraft losses')
plt.xlabel('APC')
plt.ylabel('aircraft')
plt.show()

#create a figure with 2 subplots to show the distribution of losses and aircraft losses
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
