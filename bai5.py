s = input("Nhập chuỗi: ")
so = []
temp = ""

for c in s:
    if '0' <= c <= '9':
        temp += c
    else:
        if temp != "":
            so.append(temp)
            temp = ""

if temp != "":
    so.append(temp)

if len(so) > 0:
    print("Các số tìm được:", so)
else:
    print("Không có số trong chuỗi.")