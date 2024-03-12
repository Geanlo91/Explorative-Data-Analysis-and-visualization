import pandas as pd
import requests


data = pd.read_csv('russia_losses_equipment.csv')



# clean the data and replace the missing values with 0
clean_data = data.fillna(0)
print(clean_data.head())

#save the clean data to a new csv file
clean_data.to_csv('clean_russia_losses_equipment.csv', index=False)




