import datetime
from genk import get_24h_articles
while True:

    #1. lấy giờ hiện tại so sánh với 8h
    current_time = datetime.datetime.now()
    print("giờ hiện tại: ",current_time)
    int_hour = current_time.hour
    if int_hour == 13:

    #2. lấy dư liệu trang genk/24k
        print("2. LẤY DỮ LIỆU TRANG GENK")
        get_24h_articles()

