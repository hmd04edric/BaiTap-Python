import pandas as pd

input_dict = {
    "Name": ["An", "Bình", "Chi","Đạt","Nam","Lan","Nhung","Quân","Long","Linh"],
    "Age": [20, 21, 19, 19, 20, 21, 19, 20, 21, 19],
    "Gender": ["Nam", "Nữ", "Nữ", "Nam", "Nam", "Nữ", "Nữ","Nam", "Nam", "Nữ"],
    "Score": [7.3, 2, 5.5, 10, 9, 8.5, 8, 7, 7.5, 6]
}
df = pd.DataFrame(input_dict)
# Toàn bộ dữ liệu của bảng
print(df)
# 3 dòng đầu tiên
print(df.head(3))
# Theo index=2 và cột Name
print(df.loc[2, "Name"])
# Theo index=10 và cột Age
if 10 in df.index:
    print(df.loc[10, "Age"])
else:
    print("Index 10 không tồn tại.")
# Các cột Name và Score
print(df[["Name", "Score"]])
# theem cot Pass
df["Pass"] = df["Score"] >= 5
#sap xep
df_sorted = df.sort_values(by="Score", ascending=False)
print(df)