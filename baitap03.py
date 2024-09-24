from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# khởi tạo webdriver
driver = webdriver.Chrome()

# mở trang
url= "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22P%22"
driver.get(url);

time.sleep(2)
#lay ra tat ca the ul
ul_tag = driver.find_elements(By.TAG_NAME, "UL")

#chon the ul thu 2
ul_painters = ul_tag[20] # list start with index = 0

#lay ra tat ca the <li> thuoc ul_painters
li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

#tao danh sach cac url
links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href")for tag in li_tags]
# lay danh sach ten cac url
titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title")for tag in li_tags]

#in ra url
for link in links:
    print(link)
# in ra title
for title in titles:
    print(title)

#dong webdrive
driver.quit()