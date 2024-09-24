from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

######################################################
# I. Tạo danh sách chứa links và DataFrame rỗng
all_links = []
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

######################################################
# II. Lấy ra tất cả đường dẫn để truy cập đến họa sĩ
# Khởi tạo Webdriver
for i in range(65,91):
    driver = webdriver.Chrome()
    url = f"https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22{chr(i)}%22"
    try:
        # Mở trang
        driver.get(url)

        # Đợi một chút để trang tải
        time.sleep(3)

        # Lấy ra tất cả các thẻ ul
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")
        print(len(ul_tags))

        # Chọn thẻ ul thứ 21
        ul_painters = ul_tags[20]  # danh sách bắt đầu với chỉ số = 0

        # Lấy ra tất cả các thẻ <li> thuộc ul_painters
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        # Tạo danh sách các url
        links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
        all_links.extend(links)  # Thêm tất cả các liên kết vào danh sách
    except Exception as e:
        print(f"Error while retrieving links: {e}")

    # Đóng webdriver
    driver.quit()

######################################################
# III. Lấy thông tin của từng họa sĩ
for link in enumerate(all_links):
    print(link)
    try:
        # Khởi tạo webdriver cho từng họa sĩ
        driver = webdriver.Chrome()
        driver.get(link)
        time.sleep(2)

        # Lấy tên họa sĩ
        try:
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""

        # Lấy ngày sinh
        try:
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            birth = birth_element.text
            birth_match = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth)
            birth = birth_match[0] if birth_match else ""
        except:
            birth = ""

        # Lấy ngày mất
        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = death_element.text
            death_match = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)
            death = death_match[0] if death_match else ""
        except:
            death = ""

        # Lấy quốc tịch
        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
            nationality = nationality_element.text
        except:
            nationality = ""

        # Tạo dictionary thông tin của họa sĩ
        painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}

        # Chuyển đổi dictionary thành DataFrame và thêm vào DataFrame chính
        painter_df = pd.DataFrame([painter])
        d = pd.concat([d, painter_df], ignore_index=True)

    except Exception as e:
        print(f"Error retrieving data for {link}: {e}")

    # Đóng webdriver sau khi lấy thông tin
    driver.quit()

####################
# IV. In thông tin
print(d)
# Đặt tên file
file_name = 'Painters.xlsx'

# Lưu vào file Excel
d.to_excel(file_name, index=False)  # index=False để không lưu chỉ số
print('DataFrame is written to Excel file successfully.')
