class dog:
    def __init__(self, name, age, loai):
        self.name = name
        self.age = age
        self.loai = loai
    def thong_tin(self):
        print(f'Pet của toi là chó, nó tên là {self.name}, năm nay nó {self.age} tuổi, nó thuộc loài {self.loai}')

gau = dog('Gấu',4,'Ngao tây tạng')
gau.thong_tin()