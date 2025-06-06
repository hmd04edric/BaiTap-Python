import pandas as pd
import numpy as np

# bảng Nhân viên
employee_data_dict = {
    'ID': [101, 102, 103, 104, 105, 106],
    'Name': ['An', 'Bình', 'Cường', 'Dương', np.nan, 'Hạnh'],
    'Age': [25, np.nan, 30, 22, 28, 35],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', np.nan],
    'Salary': [700, 800, 750, np.nan, 710, 770]
}
df_nv = pd.DataFrame(employee_data)

# bảng Phòng ban
department_data_dict = {
    'Department': ['HR', 'IT', 'Finance', 'Marketing'],
    'Manager': ['Trang', 'Khoa', 'Minh', 'Lan']
}
df_pb = pd.DataFrame(department_data)

# Kiểm tra các ô dữ liệu bị thiếu
print("Dữ liệu bị thiếu trong bảng Nhân viên:")
print(df_nv.isnull())

# Xoá dòng có hơn 2 giá trị bị thiếu
df_nv = df_nv[df_nv.isnull().sum(axis=1) <= 2]

# Điền giá trị cho các ô bị thiếu
df_nv['Name'].fillna('Chưa rõ', inplace=True)
df_nv['Age'].fillna(df_nv['Age'].mean(), inplace=True)
df_nv['Salary'].fillna(method='ffill', inplace=True)
df_nv['Department'].fillna('Unknown', inplace=True)

#  Chuyển kiểu dữ liệu Age và Salary sang int
df_nv['Age'] = df_nv['Age'].astype(int)
df_nv['Salary'] = df_nv['Salary'].astype(int)

#  Tạo cột Salary_after_tax = Salary * 0.9
df_nv['Salary_after_tax'] = (df_nv['Salary'] * 0.9).astype(int)

#  Lọc nhân viên phòng IT và tuổi > 25
nv_it_gt25 = df_nv[(df_nv['Department'] == 'IT') & (df_nv['Age'] > 25)]
print("Nhân viên phòng IT và tuổi > 25:")
print(nv_it_gt25)

#  Sắp xếp theo Salary_after_tax giảm dần
df_nv_sorted = df_nv.sort_values(by='Salary_after_tax', ascending=False)
print("Bảng Nhân viên sau khi sắp xếp theo Salary_after_tax giảm dần:")
print(df_nv_sorted)

#  Nhóm theo Department và tính lương trung bình
avg_salary_by_dept = df_nv.groupby('Department')['Salary'].mean()
print("Mức lương trung bình theo phòng ban:")
print(avg_salary_by_dept)

#  merge 
df_merged = pd.merge(df_nv, df_pb, on='Department', how='left')
print("Bảng nhân viên kèm tên Manager:")
print(df_merged)

#Tạo bảng Nhân viên mới và thêm vào bảng chính
nhan_vien_moi = pd.DataFrame({
    'ID': [107, 108],
    'Name': ['Hùng', 'Loan'],
    'Age': [27, 26],
    'Department': ['IT', 'Marketing'],
    'Salary': [780, 750]
})
nhan_vien_moi['Salary_after_tax'] = (nhan_vien_moi['Salary'] * 0.9).astype(int)

# Gộp bảng nhân viên
df_nv_final = pd.concat([df_nv, nhan_vien_moi], ignore_index=True)
print("Bảng Nhân viên sau khi thêm nhân viên mới:")
print(df_nv_final)
