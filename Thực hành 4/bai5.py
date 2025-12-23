def dictionary(ds):
    for i in ds:
        return f'{i} -> {ds[i]}'

dict = {
    'Love': 'Yêu',
    'Like': 'Thích'
}
print(dictionary(dict))