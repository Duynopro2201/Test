#Tạo Set#
Ten={'Long','Duy','Tú'}
print(Ten)

numbers=(1,2,3,2,4,2)
num_set=set(numbers)
print(num_set)

empty_set=set()

#Thêm phần tử#
Ten.add('Hùng')
print(Ten)

#Xóa phần tử#
Ten.remove('Long')
Ten.discard('Tú')
Ten.pop()
Ten.clear()

#Duyệt qua các phần tử trong set
Fruits={'Apple','Banana','Cherry'}
for Fruit in Fruits:
    print(Fruit)
 
#Duyệt set kết hợp điều kiện
for i in num_set:
    if i % 2 != 0:
        print(f'{i} là số lẻ')

#Duyệt và tạo set mới
squares={i**3 for i in range(1,6)}
print(squares)

#Một số hàm thông dụng với set
Hoa_qua=Fruits.copy()
print(len(Hoa_qua))
print('Apple' in Hoa_qua)
print('mango' not in Hoa_qua)


  