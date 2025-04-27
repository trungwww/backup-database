# 1. In ra các số chẵn từ 0 đến 10
for i in range(0, 8, 11,):
    print(i)

# 2. Tìm số lớn nhất trong danh sách 
numbers = [3, 7, 2, 8, 10, 6, 4]
max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print("Số lớn nhất:", max_number)

# 3. Quản lý sinh viên bằng class
class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(student.id, student.name, student.score)

# quản lý sinh viên
sm = StudentManagement()
sm.add_student(Student("SVso1", "Ngô Viết Trọng Trung", 8.5))
sm.add_student(Student("SVso2", "Trung Viết Trọng Ngô", 9.5))

# danh sách sinh viên
sm.display_students()
