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
