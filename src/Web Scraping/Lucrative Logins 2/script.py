# The Datathon Team is curious how many goals were scored
# at a Rocket League Tournament. Similar to the last question,
# we have given you a website to log into, and beyond that is a
# lot of data about Rocket League on many different pages. In
# order to obtain the flag, you must report how many total
# goals were scored in the tournament.

import requests
from bs4 import BeautifulSoup
import pandas as pd

login_url = "https://webscrape2-dot-chunin.uc.r.appspot.com/login"
credintials = {
    "username": "datathon_participant",
    "password": "pagination!"
}

with requests.session() as req:
    page = req.get(url=login_url)
    soup = BeautifulSoup(page.text, features="lxml")
    secret = soup.find("input", type="hidden", attrs={"name":"secret"})
    credintials["secret"] = secret["value"]
    page = req.post(url=login_url, data=credintials)
    
    page_url = "https://webscrape2-dot-chunin.uc.r.appspot.com/api/data?page="
    goal_sum = 0
    for i in range(1,21):
        url=page_url+str(i)
        page = req.get(url=url)
        
        table = pd.DataFrame(list(eval(page.text)))
        goal_sum += sum(table["core_goals"].astype(float))
    print(f"sum of goals: {goal_sum}")
    