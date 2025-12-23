n = int(input())
sv = {}
for i in range(n):
    msv = input()
    ten = input()
    lop = input()
    sv[msv] = [ten, lop]

cc = {}
for i in range(n):
    chuyencan = input().split()
    msv = chuyencan[0]
    chuoi = chuyencan[1]
    cc[msv] = chuoi
    
for ma in sv:
    ten, lop = sv[ma]
    chuoi = cc[ma]
    diem = 10 - chuoi.count('m') - chuoi.count('v')*2
    if diem <= 0:
        print(ma,ten,lop,diem,'DKKD')
    else:
        print(ma,ten,lop,diem)
        
    
    

    