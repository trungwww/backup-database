import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Truy cập trang web
url = "https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/3/da-nang.html"

try:
    response = requests.get(url)
    response.raise_for_status()  # Kiểm tra mã trạng thái HTTP
    soup = BeautifulSoup(response.content, "html.parser")

    # Lấy dữ liệu
    titles = []
    descriptions = []
    areas = []
    prices = []
    addresses = []

    # Duyệt qua từng mục trên trang
    list_data = soup.find_all("div", class_="listing-item")

    if list_data:
        for listing in list_data:
            try:
                title = listing.find("h3", class_="title").text.strip() if listing.find("h3", class_="title") else "N/A"
                description = listing.find("p", class_="description").text.strip() if listing.find("p", class_="description") else "N/A"
                area = listing.find("span", class_="area").text.strip() if listing.find("span", class_="area") else "N/A"
                price = listing.find("span", class_="price").text.strip() if listing.find("span", class_="price") else "N/A"
                address = listing.find("span", class_="address").text.strip() if listing.find("span", class_="address") else "N/A"

                titles.append(title)
                descriptions.append(description)
                areas.append(area)
                prices.append(price)
                addresses.append(address)
            except AttributeError as e:
                print(f"Lỗi khi xử lý một mục: {e}")

        # Lưu dữ liệu vào file Excel hoặc CSV
        data = {
            "Tiêu đề": titles,
            "Mô tả": descriptions,
            "Diện tích": areas,
            "Giá": prices,
            "Địa chỉ": addresses,
        }
        df = pd.DataFrame(data)

        # Lưu file CSV
        df.to_csv("du_lieu_nha_dat.csv", index=False, encoding="utf-8")
        print("Dữ liệu đã được lưu vào file du_lieu_nha_dat.csv ")

    else:
        print("Không tìm thấy dữ liệu trên trang web.")

except requests.exceptions.RequestException as e:
    print(f"Lỗi kết nối: {e}")
except Exception as e:
    print(f"Lỗi không xác định: {e}")