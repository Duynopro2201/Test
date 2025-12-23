def ktra(ds, ptu):
    return ptu in ds

tuple = input('Nhập tất cả các kí tự ( cách nhau bởi dấu cách):')
tuple1 = tuple.split()
x = input('Kí tự cần kiểm tra:')
print(ktra(tuple1,x))