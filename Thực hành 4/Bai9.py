def cong_dict(dict1, dict2):
    kq = dict1.copy()
    for key, value in dict2.items():
        if key in kq:
            kq[key] += value
        else:
            kq[key] = value
    print(kq)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 5, 'c': 7, 'd': 4}
cong_dict(dict1, dict2)
            
        