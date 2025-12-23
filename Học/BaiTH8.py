
chuoi = input("Nhập vào các số nguyên cách nhau bởi dấu cách: ")
day_so = list(map(int, chuoi.split()))
print("Danh sách số vừa nhập là:", day_so)
tong=sum(day_so)
print('Tổng của dãy số là:',tong)
print('Trung bình của dãy số là',tong/len(day_so))
print('Số lớn nhất trong dãy là:',max(day_so))
