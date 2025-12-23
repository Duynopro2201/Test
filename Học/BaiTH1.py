Chuoi=input('Nhập chuỗi của bạn:')
print('Chuỗi bạn  có',len(Chuoi),'kí tự')
for i in set(Chuoi):
    print(i,':',Chuoi.count(i),'lần')