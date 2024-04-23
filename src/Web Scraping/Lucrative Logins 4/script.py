#The Datathon Team owns a Starbucks in New York. 
# Unfortunately, they haven't kept up with the website much. 
# Lots of users have been leaving reviews, but we can't 
# respond to all of them. We want you to go in and respond to
# all of the users. Each user has left a rating between 1 and 5,
# and we have left some guidelines on what to respond with
# corresponding to each rating. In order to obtain the flag, you
# must respond to each user with the correct response. One of
# them will reply back to you with the flag in the form of
# 'flag{random}'. You will report 'flag{random}' in your
# submission for the flag.

# Response Guidelines:

# Rating = 1: We're sorry to hear about your experience. Could you share more details so we can address your concerns?
# Rating = 2: Thanks for your feedback. We'll use it to improve. Any specific suggestions?
# Rating = 3: Appreciate your feedback! We'll work on areas needing improvement.
# Rating = 4: Thanks for the positive feedback! We'll keep it up.
# Rating = 5: Thank you for the great review! We hope to see you again soon!

from selenium import webdriver
from bs4 import BeautifulSoup
import time

login_url = "https://webscrape4-dot-chunin.uc.r.appspot.com/login"
responses = {
    "Rating: 1": "We're sorry to hear about your experience. Could you share more details so we can address your concerns?",
    "Rating: 2": "Thanks for your feedback. We'll use it to improve. Any specific suggestions?",
    "Rating: 3": "Appreciate your feedback! We'll work on areas needing improvement.",
    "Rating: 4": "Thanks for the positive feedback! We'll keep it up.",
    "Rating: 5": "Thank you for the great review! We hope to see you again soon!"
}

edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True 
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
edge_options.add_argument('--log-level=3')

with webdriver.Edge(options=edge_options) as driver:
    driver.get(login_url)
    driver.find_element("xpath", "//select/option[@value='admin']").click()
    driver.find_element("xpath", "//input[@name='id_no']").send_keys("1234")
    driver.find_element("xpath", "//input[@name='password']").send_keys("s3lenium!")
    driver.find_element("xpath", "//input[@type='submit']").click()

    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(.5)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
    
    ratings = driver.find_elements("xpath", "//*[@id='post-container']/div[*]/p[3]")
    text_inputs = driver.find_elements("xpath", "//*[@id='post-container']/div[*]/input")
    buttons = driver.find_elements("xpath", "//*[@id='post-container']/div[*]/button")
    
    for i in range(len(ratings)):
        rating = ratings[i].text
        text_inputs[i].send_keys(responses[rating])
        buttons[i].click()
    
    comments = driver.find_elements("class name", "comments-list")    
    comments = list(map(lambda x: x.text if "flag" in x.text else "" , comments))
    comment = list(filter(str.strip, comments))[0]
    flag = comment[comment.index("{"):comment.index("}")+1]
    driver.quit()
print(f"The flag is: flag{flag}")