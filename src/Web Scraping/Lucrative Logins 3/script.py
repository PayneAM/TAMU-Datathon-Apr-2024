# The Datathon Team's database got hacked and encrypted!
# Fortunately, the hacker has left behind a website that
# requires login credentials, granting us access to our
# database! They have provided us with a tool on the page that
# can decrypt the encrypted text. We are curious where our
# datapoint "datathon" is located. In this challenge, the flag
# you will report is the encrypted value of "datathon". Can you
# find it?

from bs4 import BeautifulSoup
from selenium import webdriver

login_url = "https://webscrape3-dot-chunin.uc.r.appspot.com/login"

edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True 
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
edge_options.add_argument('--log-level=3')

with webdriver.Edge(options=edge_options) as driver:
   
    driver.get(login_url)
    driver.find_element("id", "username").send_keys("datathon_participant")
    driver.find_element("id", "password").send_keys("interaction1234")
    driver.find_element("id", "login").click()
    
    soup = BeautifulSoup(driver.page_source, features="lxml")
    encrypted_data = soup.find("div", {"class":"encryptedData"}).get_text().strip().split("\n")
   
    input_encrypted_data = driver.find_element("id", "decryptionBox")
    button_decrypt= driver.find_element("id", "decrypt")
    output_decrypted = driver.find_element("id", "decrypted")
    
    def decrypt(data):
        input_encrypted_data.send_keys(data)
        button_decrypt.click()
        input_encrypted_data.clear()
        return output_decrypted.get_attribute("value")
    decrypted_data = list(map(decrypt, encrypted_data))
    driver.quit()
print(f"encrypted value is: {encrypted_data[decrypted_data.index("datathon")]}")