# You have been asked to look at and analyze baseball
# statistics for the Datathon Team. We have provided you with
# a website to log into. Beyond that is a table containing
# different stats for each team from 2006 to 2023. In order to
# obtain the flag for this challenge you must log into the
# website and report the total number of home runs hit
# between 2006 and 2023. Be careful though, there is
# something hidden on the login page which you need to find
# in order to receive access.

import requests
import pandas as pd
from io import StringIO


login_url = "https://webscrape1-dot-chunin.uc.r.appspot.com/login"
credintials = {
    "username": "datathon_participant",
    "password": "webscrape!",
    "secret": "selenium_secret"
}

with requests.session() as req:
    page = req.post(url=login_url, data=credintials)
    df = pd.read_html(StringIO(page.text))[0]
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    homeruns_sum = sum(df["homeruns"].apply(lambda x: int(x)))
    print(f"sum of homeruns: homeruns_sum")
    
    