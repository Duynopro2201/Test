def tong(a):
    tong = sum(a)
    return tong
n = list(map(int, input('Nhập dãy các số nguyên(cách nhau bởi dấu cách):').split()))
print('tổng của dãy là:',tong(n))