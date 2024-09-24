from openpyxl.styles.builtins import linked_cell
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.expected_conditions import url_changes

# khởi tạo webdriver
driver = webdriver.Chrome()
for i in range(65,67):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"
    try:
        # mở trang
        driver.get(url);

        time.sleep(5)
        # lay ra tat ca the ul
        ul_tag = driver.find_elements(By.TAG_NAME, "ul")

        # chon the ul thu 20
        ul_painters = ul_tag[20]  # list start with index = 0

        # lay ra tat ca the <li> thuoc ul_painters
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

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

        # in ra title
        for title in titles:
            print(title)
        for link in links:
            print(link)
    except:
        print("Error")
#dong webdrive
driver.quit()