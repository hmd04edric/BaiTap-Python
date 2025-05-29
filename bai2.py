s = input("Nhập chuỗi: ").strip()
words = s.split()
result = ""

for i in range(len(words)-1, -1, -1):
    result += words[i] + " "

print("Kết quả:", result.strip())