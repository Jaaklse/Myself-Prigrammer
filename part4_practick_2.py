def converter():
    '''Преобразует введенные данные в число с плавающей точкой'''
    try:
        a = input()
        print(float(a))
    except ValueError:
        print('Введенные данные не могут быть преобразованы в число с  плавающей точкой!')
converter()            