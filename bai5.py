import pandas as pd

df = pd.read_excel(r"E:\TuDongHoaQuyTrinh\exercise_data.xlsx")
print(df)

# 1. Xử lý ô trống trong cột "Ngày"
df['Ngày'] = df['Ngày'].fillna(method='ffill')

# Cách khác: Điền giá trị cụ thể
df.loc[20, 'Ngày'] = '2020/12/20'

# 2. Xử lý ô trống trong cột "Lượng calo"
# Chuyển cột "Lượng calo" về dạng số nếu chưa phải số
df['Lượng calo'] = pd.to_numeric(df['Lượng calo'], errors='coerce')

# Điền bằng giá trị trung bình
mean_calories = df['Lượng calo'].mean()
df['Lượng calo'] = df['Lượng calo'].fillna(mean_calories)

# Cập nhật thủ công tại dòng 16 và 26
df.loc[16, 'Lượng calo'] = 301
df.loc[26, 'Lượng calo'] = 201

# Cập nhật giá trị "Thời lượng" của dòng 5 thành 45
df.at[5, 'Thời lượng'] = 45  

# In toàn bộ DataFrame sau khi chỉnh sửa
print("_______________________________________________")
print(df)
df.to_excel(r"E:\TuDongHoaQuyTrinh\exercise_data.xlsx", index=False)
