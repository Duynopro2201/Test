chuoi=input('Nhập chuỗi tiếng anh cần xác định:').lower()
so_nguyen_am=0
khoang_cach=0
for i in chuoi:
    if i == 'o' or i == 'u' or i == 'i' or i == 'e' or i == 'e' or i == 'a':
        so_nguyen_am += 1
    elif i == ' ':
        khoang_cach +=1
print('Số từ nguyên âm trong chuỗi là:',so_nguyen_am)
print('Số từ nguyên dương trong chuỗi là:',len(chuoi)-so_nguyen_am-khoang_cach)