from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import getpass

# Đường dẫn đến file thực thi ChromeDriver
chrome_path = r"/Users/buiminhhuy/Downloads/chromedriver-mac-arm64/chromedriver"  #đường dẫn chromeDriver

# Khởi tạo đối tượng dịch vụ với đường dẫn ChromeDriver
ser = Service(chrome_path)

# Tạo tùy chọn cho Chrome
options = webdriver.ChromeOptions()
options.headless = False  # hiển thị giao diện

# Khởi tạo driver cho Chrome
driver = webdriver.Chrome(service=ser, options=options)

# Tạo url đăng nhập Reddit
url = 'https://www.reddit.com/login/'

# Truy cập trang đăng nhập
driver.get(url)

# Nhập thông tin người dùng
my_email = input('Please provide email: ')
my_password = getpass.getpass('Please provide your password: ')

# Dùng ActionChains để điều hướng qua các trường và nhập thông tin
actionChains = ActionChains(driver)
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)

# Nhập email và mật khẩu
actionChains.send_keys(my_email).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys(my_password + Keys.ENTER).perform()

# Đợi trang xử lý đăng nhập
time.sleep(10)

# Truy cập trang post bài
url2 = 'https://www.reddit.com/submit?type=TEXT'
driver.get(url2)
time.sleep(2)

# Điều hướng qua các trường và nhập tiêu đề, nội dung bài viết
for i in range(16):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(1)

# Nhập tiêu đề bài đăng
actionChains.send_keys('Ví dụ post').perform()

# Nhập nội dung bài đăng
actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys('Bùi Minh Huy' + Keys.ENTER).perform()

# Điều hướng để đăng bài
for i in range(4):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(1)

actionChains.key_down(Keys.ENTER).perform()

# Đợi để xem kết quả
time.sleep(15)

# Đóng trình duyệt
driver.quit()