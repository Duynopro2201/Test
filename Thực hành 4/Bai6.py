def khog_trung_lap(ds):
    dsm = []
    for i in ds:
        if i not in dsm:
            dsm.append(i)
    return dsm

list = input('Nhập tất cả các kí tự ( cách nhau bởi dấu cách):')
list1 = list.split()
print('Danh sách không trùng lặp là:',*khog_trung_lap(list1))