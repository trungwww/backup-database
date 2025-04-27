from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://sinhvien.dau.edu.vn/sinh-vien-dang-nhap.html')

# print(driver.title)

id_input = "UserName"
elenment_input = driver.frind_elenment(By,ID, id_input)
elenment_input.click()
elenment_input.send_keys("mã sinh siên")
driver.quit()

input("Nhấn Enter để đóng trình duyệt...")
driver.quit()