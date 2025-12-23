def Khong_trun_lap(a):
    return set(a)

list = input('Nhập tất cả các kí tự ( cách nhau bởi dấu cách):')
list1 = list.split()
print(Khong_trun_lap(list1))