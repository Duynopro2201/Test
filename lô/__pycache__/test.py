print('Chào mừng bạn đến với tài xỉu')
taikhoan = 0
print('Số dư hiện tại:', taikhoan)
nap = int(input('Mời bạn nạp tiền: '))
print('Nạp thành công:', nap)
taikhoan = taikhoan + nap
print('Số dư hiện tại:', taikhoan)

import random


while True:
    A = random.randint(1,6)
    B = random.randint(1,6)
    C = random.randint(1,6)
    a = A + B + C

    b = input('Chọn tài hay xỉu: ')
    c = int(input('Mời đặt cược: '))
    

    if c > taikhoan:
        print('Số dư không đủ')
    else:
        print('Xúc xắc 1:', A)
        print('Xúc xắc 2:', B)
        print('Xúc xắc 3:', C)
        print('Kết quả:', a)

        if 3 <= a <= 10 and b == "tài":
            print('Bạn đã thua:', c)
            taikhoan -= c
        elif 3 <= a <= 10 and b == "xỉu":
            print('Bạn đã thắng:', c)
            taikhoan += c
        elif 11 <= a <= 18 and b == "tài":
            print('Bạn đã thắng:', c)
            taikhoan += c
        elif 11 <= a <= 18 and b == "xỉu":
            print('Bạn đã thua:', c)
            taikhoan -= c

        print('Số dư hiện tại:', taikhoan)
    tieptuc = input('Bạn có muốn tiếp tục không (có/không): ')
    if tieptuc != 'có':
        rut=input('Bạn muốn rút tiền không(yes/no):')
        if rut=='yes':
            while True:
                Rut=int(input('Số tiền bạn muốn rút:'))
                if Rut<=taikhoan:
                    print('Rút thành công:',Rut)
                    taikhoan=taikhoan-Rut
                    print('Số dư hiện tại',taikhoan)
                    print('Cảm ơn bạn đã chơi!')
                    break
               
                
                else:
                    print('Số tiền rút không hợp lệ')
            break
        else:
            break
    
    
    if taikhoan==0 :
        them=input('Bạn có muốn nạp thêm không(yes/no):')
        if them == "yes":
            napthem=int(input('Số tiền muốn nạp:'))
            print('Nạp thành công',napthem)
            taikhoan=taikhoan + napthem
            print('Số dư hiện tại:',taikhoan)
        else:
            print('Cảm ơn bạn đã đã chơi')
            break
    
    
