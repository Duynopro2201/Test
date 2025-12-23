chuoi=input('Nhập một chuỗi:')
chuoi1=''
for i in chuoi:
    if i not in chuoi1:
        chuoi1 += i
print(chuoi1)