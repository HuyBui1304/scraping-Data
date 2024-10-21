from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
import time
import pandas as pd

# Đường dẫn đến file thực thi chromedriver
chrome_path = r"/Users/buiminhhuy/Downloads/chromedriver-mac-arm64/chromedriver"  # Cập nhật đúng đường dẫn đến ChromeDriver của bạn

# Khởi tạo đối tượng dịch vụ với đường dẫn chromedriver
ser = Service(chrome_path)

# Tạo tùy chọn cho Chrome
options = webdriver.ChromeOptions()
options.headless = False  # Tắt chế độ headless nếu bạn muốn hiển thị giao diện trình duyệt

# Khởi tạo driver cho Chrome
driver = webdriver.Chrome(service=ser, options=options)

# Tạo url
url = 'https://pythonscraping.com/pages/files/form.html'

# Truy cập
driver.get(url)

# Tạm dừng khoảng 2 giây
time.sleep(2)

# Tìm và điền dữ liệu vào các trường input
firstname_input = driver.find_element(By.XPATH, "//input[@name='firstname']")
lastname_input = driver.find_element(By.XPATH, "//input[@name='lastname']")

# Nhập tên và họ
firstname_input.send_keys('Bui')
time.sleep(1)
lastname_input.send_keys('Minh Huy')

# Tạm dừng 2 giây
time.sleep(2)

# Tìm nút "Submit" và click
button = driver.find_element(By.XPATH, "//input[@type='submit']")
button.click()

# Tạm dừng 5 giây để chờ kết quả
time.sleep(5)

# Đóng trình duyệt
driver.quit()