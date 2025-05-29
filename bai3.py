s = input("Nhập chuỗi: ")
max_count = 0
max_char = ''

for c in s:
    if c != ' ':
        count = 0
        for x in s:
            if x == c:
                count += 1
        if count > max_count:
            max_count = count
            max_char = c

print("Ký tự xuất hiện nhiều nhất:", max_char)
