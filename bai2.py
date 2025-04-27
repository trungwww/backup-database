import math

# 1. diện tích và chu vi hình tròn
radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius
print("Diện tích hình tròn:", area_of_circle)
print("Chu vi hình tròn:", circum_of_circle)

# nhập bán kính
radius_input = float(input("Nhập bán kính: "))
area_input = math.pi * radius_input ** 2
print("Diện tích hình tròn với bán kính:", area_input)

# 2. phần tủ lớn nhất
danh_sach = [10, 20, 30, 15, 35]
so_lon_nhat = max(danh_sach)
print("Số lớn nhất:", so_lon_nhat)

# 3. Phần tử nhỏ nhất
so_nho_nhat = min(danh_sach)
print("Số nhỏ nhất:", so_nho_nhat)

# 4. Độ dài của câu
cau = "Tôi là một sinh viên DAU"
do_dai = len(cau)
print("Độ dài của câu:", do_dai)

# 5. Đếm số từ trong câu
so_tu = len(cau.split())
print("Số từ trong câu:", so_tu)
