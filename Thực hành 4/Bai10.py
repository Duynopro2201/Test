def list_moi(list1):
    list_moi = []
    for i in list1:
        if i % 2 == 0 and i > 10:
            list_moi.append(i)
    print(list_moi)

day_so = list(map(int, input().split()))
list_moi(day_so)