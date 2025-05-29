n = int(input("Nhập số có 3 chữ số (100-999): "))

donvi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
        "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

if 100 <= n <= 999:
    tram = n // 100
    chuc_so = (n % 100) // 10
    donvi_so = n % 10

    chu = donvi[tram] + " trăm"
    if chuc_so == 0 and donvi_so != 0:
        chu += " lẻ " + donvi[donvi_so]
    else:
        if chuc_so > 0:
            chu += " " + chuc[chuc_so]
        if donvi_so > 0:
            if donvi_so == 1 and chuc_so > 1:
                chu += " mốt"
            elif donvi_so == 5:
                chu += " lăm"
            else:
                chu += " " + donvi[donvi_so]

    print("Kết quả:", chu)
else:
    print("Vui lòng nhập số trong khoảng 100 đến 999.")
