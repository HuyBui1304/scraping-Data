from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Đường dẫn đến file thực thi chromedriver
chrome_path = r"/Users/buiminhhuy/Downloads/chromedriver-mac-arm64/chromedriver"  # Cập nhật đúng đường dẫn đến ChromeDriver của bạn

# Khởi tạo đối tượng dịch vụ với đường dẫn ChromeDriver
ser = Service(chrome_path)

# Tạo tùy chọn cho Chrome
options = webdriver.ChromeOptions()
options.headless = False  # Tắt chế độ headless để hiện giao diện Chrome nếu muốn

# Khởi tạo driver cho Chrome
driver = webdriver.Chrome(service=ser, options=options)

# Tạo url
url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'

# Truy cập
driver.get(url)

# In ra nội dung của trang web
print("Before: ================================\n")
print(driver.page_source)

# Tạm dừng khoảng 3 giây
time.sleep(3)

# In lại nội dung của trang web sau 3 giây
print("\n\n\n\nAfter: ================================\n")
print(driver.page_source)

# Đóng trình duyệt
driver.quit()