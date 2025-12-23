class student:
    def __init__(self, name, age, code):
        self.name = name
        self.age = age
        self.code = code
    def thong_tin(self):
        print(f'Xin chào tên tôi là {self.name}, năm nay tôi {self.age} mã sinh viên của tôi là {self.code}')

duy = student('Duy',18,'B25DCCC051')
duy.thong_tin()