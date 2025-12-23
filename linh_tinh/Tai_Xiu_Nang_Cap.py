from tkinter import *

def main():
    usename = Name.get()   #lây giá trị nhập vào từ Name = Entry
    Login.destroy()   #Đóng cửa sổ cũ

    taikhoan = 0
    
    main = Tk()
    
    Khung_main = Frame(main)
    Khung_main.pack(fill = 'x', padx=10, pady=10)
    
    main_Name = Label(Khung_main, text = usename)
    main_Name.pack(side = LEFT)
    
    BtNap = Button(Khung_main, text = '+') 
    BtNap.pack(side = RIGHT)
    
    Lbtk = Label(Khung_main, text = taikhoan)
    Lbtk.pack(side = RIGHT, padx = 5)
    
    Khung_play = Frame(main, bg = 'red', padx = 10, pady = 30)
    Khung_play.pack()
    
    main.mainloop()
    
    
Login = Tk()
Login.title('Đăng nhập Tài Xỉu')

FrLogin = Frame(Login, padx = 100, pady = 10)
FrLogin.pack()
LbLogin = Label(FrLogin, text = 'Đăng Nhập', font =( 'Time New Roman', 20), fg = 'green')
LbLogin.pack()
            #Nhập tên đăng nhập
LbName = Label(FrLogin, text = 'Nhập tên đăng nhập').pack()
Name = Entry(FrLogin)
Name.pack()
            #Nhập mật khẩu
LbPass = Label(FrLogin, text = 'Nhập mật khẩu').pack()
Pass = Entry(FrLogin)
Pass.pack()


BtLogin = Button(FrLogin, text = 'Đăng nhập', command = main)
BtLogin.pack()

Login.mainloop()
