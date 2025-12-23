import datetime
from datetime import datetime
now = datetime.now()

class BankAcc():
    def __init__(self, so_du):
        self.__sd = so_du
        self.lichsu = []
    def nap(self, nap):
        if nap <= 0:
            raise ValueError("Số tiền nạp phải lớn hơn 0!")
        self.__sd += nap 
        self.lichsu.append(f'Nạp thành công {nap} VNĐ vào tài khoản \nSố dư hiện tại là: {self.__sd}vnd \n({now})\n ')
        
    def rut(self, rut):
        if rut <= 0:
            raise ValueError("Số tiền nạp phải lớn hơn 0!")
        elif rut > self.__sd:
            raise ValueError("Số tiền rút vượt quá số dư!")
        self.__sd -= rut
        self.lichsu.append(f'Rút thành công {rut} VNĐ \nSố dư còn lại là:{self.__sd} VNĐ \n({now})\n ')
    def xem(self):
        return  self.__sd
acc1 = BankAcc(100000)
acc1.rut(10000)
acc1.nap(20000)

print("Số dư:", acc1.xem())
print("Lịch sử giao dịch:\n")
for t in acc1.lichsu:
    print(t)