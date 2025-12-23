a=input('Em tên gì:')
print('Hello',a)
x = int(input('Em gái nam nay bao tuổi rồi:'))
if x >= 18:
    y = input('Em có người yêu chữa?(yes/no):')
    if y == 'no':
        t = input('Hen hò với anh em nhé <3(yes/no):')
        if t == 'yes':
            print('I Love U BBi')
        elif t == 'no':
            print('SAo en phũ thế, chúc em hạnh phúc đanh qua cầu Nhật Tân đây T-T')
        
    elif y == 'yes':
        print('Thế thì cút, tốn cả nước bọt')

else:
    print('Xuống hầm e nhé, ko thì cút!')

