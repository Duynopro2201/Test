def max(ds):
    lon_nhat = -99999
    for i in ds:
        if i > lon_nhat:
            lon_nhat = i
    return lon_nhat

n = list(map(int, input('Nhập dãy các số nguyên(cách nhau bởi dấu cách):').split()))
print('Số lớn nhất trong dãy là:',max(n))
        