import os
import shutil
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from dotenv import load_dotenv

# Load thông tin từ file .env
load_dotenv()

# Đọc thông tin từ môi trường
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
APP_PASSWORD = os.getenv('APP_PASSWORD')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')

# Hàm gửi email
def send_email(subject, body):
    # Tạo message
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = RECEIVER_EMAIL
    message['Subject'] = subject

    # Thêm nội dung email (sử dụng UTF-8)
    message.attach(MIMEText(body, 'plain', 'utf-8'))

    # Kết nối đến server Gmail
    try:
        print("Đang kết nối đến server Gmail...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Bảo mật kết nối
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        # Gửi email
        text = message.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
        print(f"Email đã được gửi đến {RECEIVER_EMAIL}")

        # Đóng kết nối
        server.quit()

    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")

# Hàm sao lưu database
def backup_database():
    # Đọc thời gian hiện tại
    current_time = datetime.datetime.now()

    # Chỉnh lại thời gian sao lưu là 00:00 (12h đêm)
    backup_time = datetime.time(0, 0)  # 00:00 AM (nửa đêm)
    print(f"Chương trình sao lưu tự động đang chạy... Dự kiến backup lúc {backup_time}")

    # Thư mục lưu database và backup
    source_dir = 'database'   # Thư mục chứa file .sql, .sqlite3
    backup_dir = 'backup'     # Thư mục chứa file backup

    # Kiểm tra thư mục backup, nếu chưa có thì tạo mới
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"Tạo thư mục backup: {backup_dir}")

    # Duyệt qua tất cả file trong thư mục source_dir
    files_backed_up = False
    for file_name in os.listdir(source_dir):
        if file_name.endswith('.sql') or file_name.endswith('.sqlite3'):
            file_path = os.path.join(source_dir, file_name)
            backup_path = os.path.join(backup_dir, file_name)

            # Copy file từ source đến backup
            try:
                shutil.copy(file_path, backup_path)
                print(f"Đã sao lưu file: {file_name}")
                files_backed_up = True
            except Exception as e:
                print(f"Lỗi sao lưu file {file_name}: {e}")

    if files_backed_up:
        # Gửi email thông báo
        subject = "Thông báo sao lưu tự động"
        body = "Quá trình sao lưu đã hoàn tất thành công."
        send_email(subject, body)
    else:
        print("Không có file để sao lưu.")

if __name__ == "__main__":
    # Lặp lại mỗi ngày cho đến 00:00
    while True:
        current_time = datetime.datetime.now()
        print(f"Kiểm tra thời gian: {current_time}")
        if current_time.hour == 0 and current_time.minute == 0:  # Nếu là 00:00
            print("Đến thời gian sao lưu!")
            backup_database()
            # Ngủ 60 giây (1 phút) để tránh sao lưu lại trong cùng 1 phút
            time.sleep(60)
        else:
            # Ngủ 30 giây và kiểm tra lại thời gian
            print("Chưa đến thời gian sao lưu, kiểm tra lại sau 30 giây.")
            time.sleep(30)
