n= int(input())
for i in range(n):
    x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))
    canh1 = round(((x1 + x2)**2 + (y1 +y2)**2)**(1/2),3)
    canh2 = round(((x1 + x3)**2 + (y1 +y3)**2)**(1/2),3)
    canh3 = round(((x3 + x2)**2 + (y3 +y2)**2)**(1/2),3)
    if canh1 + canh2 >= canh3 and canh2 + canh3 >= canh1 and canh1 + canh3 >= canh2:
        print(round((canh1 + canh2 + canh3),3))
    else:
        print('INVALID')
        