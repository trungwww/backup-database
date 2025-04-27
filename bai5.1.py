import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Gửi HTTP request đến trang web
response = requests.get("https://www.24h.com.vn/tin-tuc-cong-nghe-c453.html")

# 2. Kiểm tra nếu request thành công
if response.status_code == 200:
    # 3. Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # 4. Tìm kiếm các bài viết
    articles = soup.find_all("article", class_="item-news")  # Điều chỉnh class nếu cần thiết

    data = []
    for article in articles:
        # 5. Trích xuất tiêu đề
        title = article.find("h3", class_="title").text.strip()  # Điều chỉnh class nếu cần thiết

        # 6. Trích xuất tóm tắt
        summary = article.find("p", class_="sapo").text.strip()  # Điều chỉnh class nếu cần thiết

        # 7. Trích xuất nội dung (có thể chứa HTML)
        content = str(article.find("div", class_="content-news"))  # Điều chỉnh class nếu cần thiết

        # 8. Trích xuất link ảnh (nếu có)
        img_tag = article.find("img")
        image_link = img_tag["src"] if img_tag else None

        # 9. Thêm dữ liệu vào danh sách
        data.append({
            "title": title,
            "summary": summary,
            "content": content,
            "image_link": image_link
        })

    # 10. Tạo DataFrame từ dữ liệu
    df = pd.DataFrame(data)

    # 11. In hoặc lưu DataFrame
    print(df.head())  # In vài dòng đầu để kiểm tra
    # df.to_csv("24h_cong_nghe.csv", index=False, encoding="utf-8-sig")  # Lưu vào file CSV

else:
    print(f"Lỗi khi truy cập trang web: {response.status_code}")