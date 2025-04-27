#import math
#radius = 30
#area_of_circle = math.pi * radius ** 2
#circum_of_circle = 2 * math.pi * radius
#print("Dien tich hinh tron: ", area_of_circle)
#print("Chu vi hinh tron: ", circum_of_circle)
#import math
#radius = float(input("Nhap ban kinh hinh tron: "))
#area_of_circle = math.pi * radius ** 2
#circum_of_circle = 2 * math.pi * radius
#print("Dien tich hinh tron:", area_of_circle)
#print("Chu vi hinh tron: ", circum_of_circle)

#for i in range(11):
    #if i % 2 == 0:
        #print(i)

#numbers = [1,2,3,4,5,6,7,8,9]
#max_num = numbers[0]
#for num in numbers:
    #if num > max_num:
       # max_num = num
#print("so lon nhat: ", max_num)

#lop chat Nguoi
class Nguoi:
    #khoi tao
    def __init__(self, ten, tuoi):
        #thuoc tinh ten
        self.ten = ten
        #thuoc tinh tuoi
        self.tuoi = tuoi
    def gioi_thieu(self):
        print(f"xin chao, toi ten la (self.ten), (self.tuoi) tuoi,")

doi_tuong_nguoi = Nguoi(ten="An", tuoi=20)
print(doi_tuong_nguoi.ten)
doi_tuong_nguoi.gioi_thieu()