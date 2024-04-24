# You are a detective who has been tasked by the College
# Station Police Department to find the perpetrator who is,
# perchance, behind the infamous Veo Bike Midair
# Suspension Incident of 2024". You have been provided a
# list of residents of College Station (it's not real) to comb
# through to find the perpetrator. All you know about this
# enigmatic figure is that their phone number spelt out is
# their last name. In other words, this individual's entire last
# name is a phoneword for their entire phone number. See 
# https://en.wikipedia.org/wiki/Phoneword for clarification. 
# Provide the numerical component of this individual's address
# to the power of two as the flag.

import pandas as pd

residents_df = pd.read_csv("src\\Data Manipulation\\Data Detectives\\residents.csv")

translationdict = str.maketrans("abcdefghijklmnopqrstuvwxyz", "22233344455566677778889999")
perpetrator = residents_df[residents_df["name"].apply(lambda x: x.split()[1].lower().translate(translationdict)) == residents_df["phone"].apply(lambda x: x.replace("-", ""))]

address_pow2 = float(str(perpetrator['address']).split()[0]) ** 2
print(address_pow2)