#самостоятельно не могла справиться с заданием, переписала Ваш код, но почему то выдает
#ошибку for f in features.keys():
# AttributeError: 'set' object has no attribute 'keys'
good = []
features = {'название', 'цена', 'количество', 'единицы измерения'}
analytics = {'название': [], 'цена': [], 'количество': [], 'единицы измерения': []}
num = 0

while True:
    if input('Для выхода из приложения нажмите Q, для продолжения Enter - ').upper == 'Q':
        break
    num += 1
    for f in features.keys():
        prop = input(f'Введите значнение свойства {f} - ')
        features[f] = int(prop) if (f == 'цена' or f == 'количество') else prop
        analytics[f].append(features[f])
    good.append((num, features))
    print(f'\nструктура товаров\n{good}')
    print(f'\nтекущая аналитика по товарам\n{"*" * 30}')
    for key, value in analitics.items():
        print (f'{key[:25]:>30}: {value}')
    print('*' * 30)