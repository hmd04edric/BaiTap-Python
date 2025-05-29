s = input("Nhập họ tên: ").strip()
words = s.split()

ho_lot = ""
for i in range(len(words) - 1):
    ho_lot += words[i] + " "

ten = words[-1]

print("Họ lót:", ho_lot.strip())
print("Tên:", ten)
