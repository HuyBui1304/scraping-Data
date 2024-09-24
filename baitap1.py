from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# khởi tạo WebDriver
driver = webdriver.Chrome()

# mở một trang web
driver.get("https://gomotungkinh.com")
time.sleep(5)

# tìm phần tử img có id là "bonk"
bonk_img = driver.find_element(By.ID, "bonk")

# click liên tục vào img "bonk"
while True:
    bonk_img.click()
    print("click on the book image")
    time.sleep(0.01)