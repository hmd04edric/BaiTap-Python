s = input("Nhập chuỗi: ")
checked = ""

for c in s:
    if c not in checked:
        count = 0
        for x in s:
            if x == c:
                count += 1
        print(f"'{c}': {count} lần")
        checked += c
