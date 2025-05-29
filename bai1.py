s = input("Nhập chuỗi: ").strip()
words = s.split()
result = ""

for word in words:
    new_word = word[0].upper() + word[1:].lower()
    result += new_word + " "

print("Kết quả:", result.strip())