class ngan_hang:
    def __init__(self,name,so_du):
        self.__so_du = so_du
        self.name = name
    def xem_so_du(self):
        print('Tài khoản:',self.name)
        print('Số dư:',self.__so_du)
        
    def rut_tien(self,OTP,tien_rut):
        if OTP != 123:
            print('OTP không hợp lệ')
        elif tien_rut >= self.__so_du:
            print('Số tiền rút không hợp lệ')
        else:
            self.__so_du -= tien_rut
        
so_du = ngan_hang('Duy',5000)
so_du.xem_so_du()

so_du.rut_tien(123,1000)
so_du.xem_so_du()
