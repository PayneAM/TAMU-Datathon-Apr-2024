# You work at a restaurant that hosts matchmaking night on
# Thursday nights (sadly you cannot participate). All
# participants fill out a paper questionnaire with basic
# information and you run the information through an 
# algorithm to determine compatibility between daters. You 
# find a man and a woman who match with a compatibility of
# 100%, but sadly they both are missing key information on
# their questionnaires and both have terrible handwriting (it's
# like it was meant to be). Luckily you happen to have a
# dataset of everyone that participated in matchmaking night. 
# It is of absolute utmost importance that you play Cupid and
# unite these soulmates.
# The woman's questionnaire has the following information:
# She is a Cancer
# She was born in the year of the Tiger
# You can make out the consecutive numbers "247" in her 
# phone number
# The man's questionnaire has the following information:
# He listed a "fun fact" of his as sharing a birthday (month and
# day, not year) with Sydney Sweeney
# You can make out the consecutive letters "sh" in his name
# Your submission (flag) will be the woman's last name,
# followed by the man's last name. No spaces or
# capitalization.

import pandas as pd

daters_df = pd.read_csv("src\\Data Manipulation\\Data Daters\\daters.csv")

woman = daters_df[daters_df["birthdate"].apply(lambda x: (6, 21) < tuple(list(map(int, x.split('-')[1:]))) < (7, 22)) == True]
woman = woman[woman["birthdate"].apply(lambda x: (float(x.split("-")[0])+9)%12) == 6]
woman = woman[woman["phone"].str.contains("247")]

man = daters_df[daters_df["birthdate"].str.contains("09-12")]
man = man[daters_df["name"].str.contains("sh")]

man_last_name = man["name"].split()[1].lower()
woman_last_name = man["name"].split()[1].lower()

print(f"{woman_last_name} {man_last_name}")

