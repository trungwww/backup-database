import pandas as pd

my_dict = {
    "Tên cột 1": [1, 2, 3, 4, 5, 6, 10],
    "Tên cột 2": [1, 2, 3, 4, 5, 6, 10],
    "Tên cột 3": [10, 2, 3, 4, 5, 6, 10],
    "Tên cột 4": [111, 2, 3, 4, 5, 6, 10]
}

# Load dữ liệu vào đối tượng DataFrame
df = pd.DataFrame(my_dict)

print(df)
print(df.loc[5])
print(df.loc[[0,2,6]])
data_excel = pd.read_excel("E:\\TuDongHoaQuyTrinh\\Book1.xlsx", engine="openpyxl")
print(data_excel)
data_csv = pd.read_csv("E:\TuDongHoaQuyTrinh\data.csv")
print(data_csv)
