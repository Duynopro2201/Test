chuoi=input('Nhập chuỗi các số nguyên ( cách nhau bởi dấu cách ):')
chuoi1=list(map(int, chuoi.split()))
tong_chan=0
for i in chuoi1:
    if i%2==0:
        tong_chan += i
print('Tổng số chẵn trong dãy là:',tong_chan)
        
