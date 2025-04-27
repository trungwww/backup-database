from bs4 import BeautifulSoup

html_content = """
<div class="content-item item"><div class="ct_title_box title"><div class="ct_title"><a href="/ban-nha-mt-duong-nguyen-tat-thanh-gan-khach-san-cong-doan-hai-chau-dt-5m1-x-21m-16215655.html" class="vip">Bán nhà MT đường Nguyễn Tất Thành, gần khách sạn Công Đoàn, Hải Châu. DT 5m1 x 21m</a></div><div class="ct_date">Hôm nay</div><div class="clear"></div></div><div class="vipstar vip-0"></div><div class="thumbnail"><a href="/ban-nha-mt-duong-nguyen-tat-thanh-gan-khach-san-cong-doan-hai-chau-dt-5m1-x-21m-16215655.html"><img src="/files/properties/2025/4/3/thumbnails/016215655-1937-ban-nha-mat-tien-quan-hai-chau-chinh-chu.jpg" alt="Bán nhà MT đường Nguyễn Tất Thành, gần khách sạn Công Đoàn, Hải Châu. DT 5m1 x 21m"></a></div><div class="text"><div class="ct_brief">+ Bán nhà cấp 4 mặt tiền đường Nguyễn Tất Thành, Thanh Bình, Hải Châu, Đà Nẵng.<br>+ Diện tích đất: 110m² (5.1m x 21m). Kết cấu nhà cấp 4 tiện xây mới.<br>+ Vị trí: Tọa lạc vị trí đắc địa đoạn gần Ông Ích Khiêm, khách sạn cô... <a href="/ban-nha-mt-duong-nguyen-tat-thanh-gan-khach-san-cong-doan-hai-chau-dt-5m1-x-21m-16215655.html">&lt;&lt; xem chi tiết &gt;&gt;</a></div><div class="characteristics"><span class="road-width" title="Đường trước nhà 15m">15m</span><span class="floors" title="1 lầu">1 lầu</span><span class="bedroom" title="1 phòng ngủ">1 phòng ngủ</span></div><div class="square-direct"><div class="ct_dt"><label>Diện tích:</label> 110 m<sup>2</sup></div><div class="ct_kt"><label>KT:</label> ---</div><div class="ct_direct"><label>Hướng:</label> _</div><div class="clear"></div></div><div class="price-dis"><div class="ct_price"><label>Giá:</label> 13 tỷ </div><div class="ct_dis"><a href="/nha-dat/can-ban/nha-mat-tien/duong-nguyen-tat-thanh-quan-hai-chau-dp2656.html" title="Bán nhà Đường Nguyễn Tất Thành">Đường Nguyễn Tất Thành</a>, <a href="/nha-dat/can-ban/nha-mat-tien/phuong-thanh-binh-quan-hai-chau-px1100.html" title="Bán nhà Phường Thanh Bình">Phường Thanh Bình</a>, <a href="/nha-dat/can-ban/nha-mat-tien/da-nang/584/quan-hai-chau.html" title="Bán nhà Quận Hải Châu">Quận Hải Châu</a>, Đà Nẵng</div><div class="clear"></div></div></div><input class="memberid" type="hidden" value="856541"><div class="clear"></div></div>
"""

soup = BeautifulSoup(html_content, "html.parser")

# Lấy tiêu đề
title = soup.find("a", class_="vip").text.strip()
print("Tiêu đề:", title)

# Lấy mô tả
description = soup.find("div", class_="ct_brief").text.strip()
print("Mô tả:", description)

# Lấy diện tích
area = soup.find("div", class_="ct_dt").text.replace("Diện tích:", "").strip()
print("Diện tích:", area)

# Lấy giá
price = soup.find("div", class_="ct_price").text.replace("Giá:", "").strip()
print("Giá:", price)

# Lấy địa chỉ
address = soup.find("div", class_="ct_dis").text.strip()
print("Địa chỉ:", address)

# Lấy đường trước nhà
road_width = soup.find("span", class_="road-width").text.strip() if soup.find("span", class_="road-width") else "N/A"
print("Đường trước nhà:", road_width)

# Lấy số lầu
floors = soup.find("span", class_="floors").text.strip() if soup.find("span", class_="floors") else "N/A"
print("Số lầu:", floors)

# Lấy số phòng ngủ
bedroom = soup.find("span", class_="bedroom").text.strip() if soup.find("span", class_="bedroom") else "N/A"
print("Phòng ngủ:", bedroom)