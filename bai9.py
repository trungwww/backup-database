from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# B1: Mở trình duyệt chrome
driver = webdriver.Chrome()

# B2: Vào trang https://phatnguoixe.com
driver.get("https://phatnguoixe.com/")

# B3: Chọn Option Xe máy
css_selector_input = '#frmSubmit > label:nth-child(4) > input[type=radio]'
element_xe_may = driver.find_element(By.CSS_SELECTOR, css_selector_input)
element_xe_may.click()

# B4: Điền biển số xe máy vào ô tìm kiếm
id_bien_so = 'bienso'
element_input = driver.find_element(By.ID, id_bien_so)
value_bien_so = "43H133255"
element_input.send_keys(value_bien_so)

# B5: Click vào button kiểm tra phạt nguội
xpath_btn = '//*[@id="submit"]'
element_btn = driver.find_element(By.XPATH, xpath_btn)
element_btn.click()

time.sleep(5)  # Giả sử s = 5

# B6: Kiểm tra kết quả hiển thị phạt nguội
id_result = 'resultValue'
element_result = driver.find_element(By.ID, id_result)
result_text = element_result.text

print(result_text)
result_text = ''  # Gán chuỗi rỗng cho result_text
print()