"""
Chương trình tổng hợp 10 bài tập xử lý chuỗi trong Python
"""

def bai1():
    """
    Bài 1: Viết chương trình nhập vào một chuỗi, in ra chuỗi đó với các ký tự đầu tiên 
    được viết hoa, các ký tự còn lại viết thường.
    """
    print("\n=== BÀI 1 ===")
    s = input("Nhập chuỗi: ").strip()
    words = s.split()
    result = ""

    for word in words:
        new_word = word[0].upper() + word[1:].lower()
        result += new_word + " "

    print("Kết quả:", result.strip())

def bai2():
    """
    Bài 2: Viết chương trình nhập vào một chuỗi, in ra chuỗi đảo ngược các từ.
    """
    print("\n=== BÀI 2 ===")
    s = input("Nhập chuỗi: ").strip()
    words = s.split()
    result = ""

    for i in range(len(words)-1, -1, -1):
        result += words[i] + " "

    print("Kết quả:", result.strip())

def bai3():
    """
    Bài 3: Viết chương trình nhập vào một chuỗi, tìm ký tự xuất hiện nhiều nhất trong chuỗi.
    """
    print("\n=== BÀI 3 ===")
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

    print(f"Ký tự xuất hiện nhiều nhất: '{max_char}' với {max_count} lần")

def bai4():
    """
    Bài 4: Viết chương trình nhập vào một chuỗi, đếm số lần xuất hiện của từng ký tự trong chuỗi.
    """
    print("\n=== BÀI 4 ===")
    s = input("Nhập chuỗi: ")
    checked = ""

    for c in s:
        if c not in checked and c != ' ':
            count = s.count(c)
            print(f"'{c}': {count} lần")
            checked += c

def bai5():
    """
    Bài 5: Viết chương trình tìm tất cả các số trong chuỗi.
    """
    print("\n=== BÀI 5 ===")
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

def bai6():
    """
    Bài 6: Viết chương trình tách họ, họ lót và tên từ một chuỗi họ tên đầy đủ.
    """
    print("\n=== BÀI 6 ===")
    s = input("Nhập họ tên: ").strip()
    words = s.split()

    if len(words) > 1:
        ho = words[0]
        ten = words[-1]
        ho_lot = " ".join(words[1:-1]) if len(words) > 2 else ""
        
        print("Họ:", ho)
        if ho_lot:
            print("Họ lót:", ho_lot)
        print("Tên:", ten)
    else:
        print("Vui lòng nhập đầy đủ họ và tên.")

def bai7():
    """
    Bài 7: Viết chương trình viết hoa chữ cái đầu tiên của mỗi từ trong chuỗi.
    """
    print("\n=== BÀI 7 ===")
    s = input("Nhập chuỗi: ").strip()
    words = s.split()
    result = ""

    for word in words:
        if word:  # Bỏ qua các từ rỗng
            new_word = word[0].upper() + word[1:]
            result += new_word + " "

    print("Kết quả:", result.strip())

def bai8():
    """
    Bài 8: Viết chương trình chuyển đổi ký tự thành chữ hoa nếu là vị trí chẵn, 
    chữ thường nếu là vị trí lẻ (tính từ 0).
    """
    print("\n=== BÀI 8 ===")
    s = input("Nhập chuỗi: ")
    result = ""

    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i].lower()

    print("Kết quả:", result)

def bai9():
    """
    Bài 9: Viết chương trình kiểm tra xem một chuỗi có phải là chuỗi đối xứng hay không.
    """
    print("\n=== BÀI 9 ===")
    s = input("Nhập chuỗi: ")
    doi_xung = True

    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            doi_xung = False
            break

    if doi_xung:
        print("Chuỗi đối xứng.")
    else:
        print("Chuỗi không đối xứng.")

def bai10():
    """
    Bài 10: Viết chương trình đọc số có 3 chữ số thành chữ tiếng Việt.
    """
    print("\n=== BÀI 10 ===")
    while True:
        try:
            n = int(input("Nhập số có 3 chữ số (100-999): "))
            if 100 <= n <= 999:
                break
            else:
                print("Vui lòng nhập số trong khoảng 100 đến 999.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

    donvi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
            "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

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
            elif donvi_so == 5 and chuc_so > 0:
                chu += " lăm"
            else:
                chu += " " + donvi[donvi_so]

    print("Kết quả:", chu)

def hien_thi_menu():
    """Hiển thị menu lựa chọn bài tập"""
    print("\n=== CHƯƠNG TRÌNH TỔNG HỢP 10 BÀI TẬP XỬ LÝ CHUỖI ===")
    print("1. Viết hoa chữ cái đầu từ")
    print("2. Đảo ngược chuỗi")
    print("3. Tìm ký tự xuất hiện nhiều nhất")
    print("4. Đếm số lần xuất hiện của từng ký tự")
    print("5. Tìm tất cả các số trong chuỗi")
    print("6. Tách họ, họ lót và tên")
    print("7. Viết hoa chữ cái đầu mỗi từ")
    print("8. Chuyển đổi ký tự vị trí chẵn/lẻ")
    print("9. Kiểm tra chuỗi đối xứng")
    print("10. Đọc số thành chữ tiếng Việt")
    print("0. Thoát")

def main():
    """Hàm chính của chương trình"""
    while True:
        hien_thi_menu()
        try:
            lua_chon = int(input("\nChọn bài tập (0-10): "))
            if lua_chon == 0:
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break
            elif 1 <= lua_chon <= 10:
                # Gọi hàm tương ứng với lựa chọn
                globals()[f"bai{lua_chon}"]()
                input("\nNhấn Enter để tiếp tục...")
            else:
                print("Vui lòng chọn từ 0 đến 10.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

if __name__ == "__main__":
    main()
