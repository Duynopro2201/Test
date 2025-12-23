so = int(input('Nhập số:'))
digits = list(map(int,input('Nhập danh sách (Cách nhau bởi dấu cách):').split()))
chuoi = []
chuoi += str(so)
doi_xung = len(chuoi) // 2
#Kiểm tra đối xứng
a= True
for i in range(doi_xung):
    j = i + 1
    if chuoi[i] != chuoi[-j]:
        a = False
#Kiểm tra Thuộc digits     
b = True
for i in chuoi:
    if int(i) not in digits:
        b = False
if a and b:
    print(True)
else:
    print(False)

        
        