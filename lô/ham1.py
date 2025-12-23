def numb(a,b):
    tong=a+b
    return (tong)

def KTraCL(numb):
    if numb%2==0:
        print('Tổng là số chẵn')
    else:
        print('Tổng là số lẻ')

def KTraAD(numb):
    if numb>0:
        print('Tổng là số dương')
    else:
        print('Tổng là số âm')

tong=numb(2,3)
KTraCL(tong)
KTraAD(tong)
