#Truy cập phâng tử bằng chỉ số #
My_tuple=('Dũng','Duy','Tú','Long','Lộc')
print(My_tuple[1])
print(My_tuple[-1])

#Cắt lát#
print(My_tuple[0:4:2])
print(My_tuple[-1:-5:-2])

#Tuple lồng nhau#
Mytuple1=(('Dũng','Lộc'),('Long','Duy'),'Tú','Hùng')
print(Mytuple1[1])
print(Mytuple1[1][1])

#Duyệt qua các phần tử trong Tuple#
for Bbe in My_tuple:
    print(Bbe)
    
#Một số thao tác thường dùng#
mumbers=(1,2,3,4,5,6,7,2,4,6,8,1,3,5,7,2,6,9)
print(len(mumbers))
print(mumbers.count(1))
print(mumbers.index(9))

#Các phép toán với Tuple#
Duy=(18,19,20)
Long=(12,13,14)
Duy_Long=Duy + Long
print(Duy_Long)
print(Duy*2)

#Kiểm tra phần tử tồn tại#
print('Hùng' in My_tuple)

