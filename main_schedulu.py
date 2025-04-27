#Gọi thư viện shedule
import schedule
import time

#Định nghĩa hàm
def job(name):
    print("I'm working...")

#Lập lịch chạy tự động theo giây/phút
#cứ 2 phút chạy 1 lần
schedule.every(5).seconds.do(job, name="some_name")

while True:
    schedule.run_pending()
    time.sleep(1)

#  giờ,
schedule.every().hour.do(job)

#  ngày,
schedule.every().day.at("14:36").do(job, name="lớp 22ct2")

#  tuần
