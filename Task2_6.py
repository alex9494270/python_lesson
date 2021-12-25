#data = {}
#fields = ('название', 'цена', 'количество', 'ед.')
#for field in fields:
#   data[field] = input(f'Введите значение поля {field}: ')


goods = []
features = {'название': '', 'цена': '', 'количество': '', 'ед.': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'ед.': []}
num = 0

while True:
    if input('Для выхода нажмите Q, чтобы продолжить, нажмите Enter: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        prop = input(f'Введите значение свойства {f} - ')
        features[f] = int(prop) if f in ('цена', 'количество') else prop
        analytics[f].append(features[f])
    goods.append((num, features.copy()))
    print(f"\nСтруктура товаров\n{goods}")
    print(f"\nТекущая аналитика по товарам:\n{'*' * 30}")
    for key, value in analytics.items():
       print(f"{key[:25]:>30}: {value}")
print('*' * 30)
