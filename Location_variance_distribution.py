import statistics
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = 'clean_russia_losses_equipment.csv'
clean_data = pd.read_csv(data)

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
variance = statistics.variance(apc)
print('APC variance:', variance)

#Calculate the standard deviation for the APC column
standard_deviation = statistics.stdev(apc)
print('APC standard deviation:', standard_deviation)

#plot the location variance distribution
plt.hist(apc, bins=100, edgecolor='black')
plt.title('APC losses')
plt.xlabel('APC')
plt.ylabel('count')
plt.show()
#The plot shows that the distribution of APC losses is skewed to the right
#This means that the majority of the losses are small and a few are large
#This is consistent with the high variance and standard deviation values

sns.kdeplot(apc, shade=True)
plt.title('APC losses')
plt.xlabel('APC')
plt.ylabel('Density')
plt.show()


#plot the relationship between apc losses and tank losses
sns.scatterplot(x='day', y='aircraft', data=clean_data)
plt.title('aircraft losses vs day')
plt.xlabel('day')
plt.ylabel('aircraft')
plt.show()


fig = plt.figure()
#create figure with 6 subplots
fig, axs = plt.subplots(2, 3)
fig.suptitle('Losses vs day')
#plot the relationship between apc losses and day
axs[0, 0].plot(clean_data['day'], clean_data['APC'])
axs[0, 0].set_title('APC')
#plot the relationship between tank losses and day
axs[0, 1].plot(clean_data['day'], clean_data['tank'])
axs[0, 1].set_title('tank')
#plot the relationship between aircraft losses and day
axs[0, 2].plot(clean_data['day'], clean_data['aircraft'])
axs[0, 2].set_title('aircraft')
#plot the relationship between helicopter losses and day
axs[1, 0].plot(clean_data['day'], clean_data['helicopter'])
axs[1, 0].set_title('helicopter')
#plot the relationship between MRL losses and day
axs[1, 1].plot(clean_data['day'], clean_data['naval ship'])
axs[1, 1].set_title('naval ship ')
#plot the relationship between drone losses and day
axs[1, 2].plot(clean_data['day'], clean_data['drone'])
axs[1, 2].set_title('drone')
plt.show()

#plot the violin plot for the distribution of losses
sns.violinplot(data=clean_data['aircraft'])
plt.title('Losses distribution')
plt.show()

#plot the box plot for the distribution of losses
sns.boxplot(data=clean_data['aircraft'])
plt.title('Losses distribution')
plt.show()

#plot the box plot for the distribution of losses with strip plot
sns.boxplot(data=clean_data['aircraft'])
sns.stripplot(data=clean_data['aircraft'], color='red')
plt.title('Losses distribution')
plt.show()


#change date to days of the week and plot the losses per day of the week using a histogram for drone losses


#plot a graph with vertical lines to show the mean, median and mode of the APC losses
sns.kdeplot(apc, shade=True)
plt.axvline(mean, color='red', label='mean')
plt.axvline(geometric_mean, color='green', label='geometric mean')
plt.axvline(harmonic_mean, color='blue', label='harmonic mean')
plt.title('APC losses central tendency')
plt.xlabel('APC')
plt.ylabel('count')
plt.legend()