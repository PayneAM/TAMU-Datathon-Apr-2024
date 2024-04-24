# Aloha! The dataset in .csv format you have been provided is 
# a list of all Airbnb properties listed in the state of Hawaii as 
# of 2022. The data is not clean, missing some individual 
# values for price. The flag you have to return to complete the
# challenge is the average price of Airbnbs in the 
# neighbourhood of Lahaina. Disregard null values. 
# Round your answer to two decimal places.


import pandas as pd
import numpy as np


hawaii_bnbs_df = pd.read_csv("src\\Data Manipulation\\Hawaii Airbnb Cleaning\\hawaii_bnbs.csv")
hawaii_bnbs_df = hawaii_bnbs_df[(hawaii_bnbs_df["neighbourhood"] == "Lahaina")]
hawaii_bnbs_df = hawaii_bnbs_df.dropna(subset=["price"])
hawaii_bnbs_df["price"] = hawaii_bnbs_df["price"].apply(lambda x: x if type(x) == float else float(x[1:]))

avg_price = round(np.mean(hawaii_bnbs_df["price"].to_list()),2)

print(avg_price)