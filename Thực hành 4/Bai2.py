def xuat_hien(ds, ptu):
    return ds.count(ptu)

tuple = input('Nhập tất cả các kí tự ( cách nhau bởi dấu cách):')
tuple1 = tuple.split()
x = input('Kí tự cần đếm:')
print("Số lần xuất hiện của kí tự '",x,"' là:",xuat_hien(tuple1,x))

