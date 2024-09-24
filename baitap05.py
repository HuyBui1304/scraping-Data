import re

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# tao dataframe rong
d= pd.DataFrame({'name': [], 'birth': [], 'nationality': []})

# khoi tao webdriver
driver = webdriver.Chrome()

# mo trang
url = "https://en.wikipedia.org/wiki/Edvard_Munch"
driver.get(url)

#doi 2 giay
time.sleep(2)

try:
    name = driver.find_element(By.TAG_NAME, "h1").text
except:
    name = ""
try:
    birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
    birth = birth_element.text
    birth = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
except:
    birth = ""


try:
    death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
    death = death_element.text
    death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
except:
    death = ""

try:
    nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
    nationality = nationality_element.text
except:
    nationality = ""

# tao dictionary thong tin cua hoa si
painter = {'name' :name, 'birth': birth, 'death': death, 'nationality':nationality}

# chuyen doi dictionary thanh dataframe

painter_df = pd.DataFrame([painter])

# them thong tin vao df chinh
d = pd.concat([d,painter_df], ignore_index= True)

print(d)
driver.quit()