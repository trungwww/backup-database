import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
from email.mime.text import MIMEText

# Cấu hình thông tin email
sender_email = "your_email@gmail.com"  # Thay bằng email của bạn
sender_password = "your_password"  # Thay bằng mật khẩu email của bạn
receiver_email = "recipient_email@example.com"  # Thay bằng email người nhận
subject = "Thông báo phạt nguội xe máy"

def check_phat_nguoi(bien_so):
    """
    Hàm kiểm tra phạt nguội cho biển số xe máy.

    Args:
        bien_so (str): Biển số xe máy cần kiểm tra.

    Returns:
        str: Nội dung thông báo phạt nguội (nếu có), hoặc thông báo không có phạt nguội,
             hoặc None nếu có lỗi xảy ra.
    """
    try:
        # B1: Mở trình duyệt chrome (chạy ẩn danh)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Chạy ẩn danh
        driver = webdriver.Chrome(options=options)

        # B2: Vào trang https://phatnguoixe.com
        driver.get("https://phatnguoixe.com/")

        # B3: Chọn Option Xe máy
        css_selector_input = '#frmSubmit > label:nth-child(4) > input[type=radio]'
        element_xe_may = driver.find_element(By.CSS_SELECTOR, css_selector_input)
        element_xe_may.click()

        # B4: Điền biển số xe máy vào ô tìm kiếm
        id_bien_so = 'bienso'
        element_input = driver.find_element(By.ID, id_bien_so)
        element_input.send_keys(bien_so)

        # B5: Click vào button kiểm tra phạt nguội
        xpath_btn = '//*[@id="submit"]'
        element_btn = driver.find_element(By.XPATH, xpath_btn)
        element_btn.click()

        time.sleep(5)  # Đợi trang tải kết quả

        # B6: Kiểm tra kết quả hiển thị phạt nguội
        id_result = 'resultValue'
        element_result = driver.find_element(By.ID, id_result)
        result_text = element_result.text

        return result_text

    except Exception as e:
        print(f"Lỗi khi kiểm tra phạt nguội: {e}")
        return None
    finally:
        driver.quit()

def send_email(subject, body, receiver_email):
    """
    Hàm gửi email thông báo.

    Args:
        subject (str): Tiêu đề email.
        body (str): Nội dung email.
        receiver_email (str): Địa chỉ email người nhận.
    """
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email đã được gửi thành công!")
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")

if __name__ == "__main__":
    bien_so_can_kiem_tra = "43H133255"  # Thay bằng biển số xe bạn muốn kiểm tra

    while True:
        now = datetime.datetime.now()
        # Kiểm tra nếu hiện tại là 7 giờ sáng
        if now.hour == 7 and now.minute == 0:
            print("Đang kiểm tra phạt nguội...")
            ket_qua_phat_nguoi = check_phat_nguoi(bien_so_can_kiem_tra)

            if ket_qua_phat_nguoi is not None:
                if ket_qua_phat_nguoi.strip():  # Kiểm tra nếu có nội dung phạt nguội
                    body = f"Thông báo phạt nguội cho biển số xe: {bien_so_can_kiem_tra}\n\n"
                    body += f"Kết quả kiểm tra:\n{ket_qua_phat_nguoi}\n\n"
                    body += "Vui lòng kiểm tra chi tiết trên trang web."
                    send_email(subject, body, receiver_email)
                else:
                    body = f"Không có thông tin phạt nguội cho biển số xe: {bien_so_can_kiem_tra} vào thời điểm hiện tại."
                    send_email(subject, body, receiver_email)

            # Đợi một ngày trước khi kiểm tra lại (để tránh gửi email nhiều lần trong ngày)
            time.sleep(24 * 60 * 60)  # 24 giờ * 60 phút * 60 giây
        else:
            # Chờ một khoảng thời gian ngắn trước khi kiểm tra lại thời gian
            time.sleep(60)  # Chờ 1 phút