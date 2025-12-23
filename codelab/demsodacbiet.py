def sum(a):
    tong = 0
    for i in str(a):
        tong += int(i)
    return tong
n = int(input('Nhập số:'))
tong = 0
so_so = 0
for i in range(n):
    if str(7) in str(i):
        if sum(i) % 5 == 0:
            so_so += 1   
print(so_so)