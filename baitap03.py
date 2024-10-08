from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo webdriver
driver = webdriver.Chrome()

# Mở trang
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22B%22"
driver.get(url)

# Đợi trang tải
time.sleep(2)

# Lấy ra tất cả thẻ ul
ul_tag = driver.find_elements(By.TAG_NAME, "ul")

# Chọn thẻ ul thứ 20
ul_painters = ul_tag[20]  # Danh sách bắt đầu từ index 0

# Lấy ra tất cả thẻ <li> thuộc ul_painters
li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

# Tạo danh sách các url và tiêu đề với try-except
links = []
titles = []

for tag in li_tags:
    try:
        links.append(tag.find_element(By.TAG_NAME, "a").get_attribute("href"))
        titles.append(tag.find_element(By.TAG_NAME, "a").get_attribute("title"))
    except Exception as e:
        # Nếu không tìm thấy thẻ <a> hoặc có lỗi, bỏ qua và in ra thông báo lỗi nếu cần
        print(f"Lỗi khi lấy thông tin từ thẻ <li>: {e}")
        continue




# In ra URL
for link in links:
    print(link)

# In ra title
for title in titles:
    print(title)

# Đóng webdriver
driver.quit()
