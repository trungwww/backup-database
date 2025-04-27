from selenium import webdriver
from selenium.webdriver.common.by import By

#1. mở trình duyệt
driver = webdriver.Chrome()

#2. vào web
for i in range(1,6):
    driver.get("https://alonhadat.com.vn/nha-dat/can-ban/nha-mat-tien.html")
    
#3. lấy danh sách tiêu đề
xpath_titles = 
elenment_title = driver.find_element(By.XPATH, xpath_titles)
print(elenment_tile)

#4. lấy danh sách mô tả

xpath_des = '//*[@id="left"]/div[1]/div[1]/div[4]/div[1]'
elenment_des = driver.find_elements(By.XPATH, xpath_des)
print(elenment_des)

for index, elenment in enumerate(elenment_titles);
    title = elenment.text
    description = elenment_des[index].text
    print("mô tả; ", description)    
#5. lấy danh sách giá
#6. lấy danh sach diện tích
#7. lấy danh sách địa chỉ