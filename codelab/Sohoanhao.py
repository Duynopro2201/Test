So_n = int(input('Nhập số nguyên dương n:'))
tong = 0
for i in range(1,So_n):
    if So_n % i == 0:
        tong += i
        print(tong)
if tong == So_n:
    print('True')
else:
    print('False')
