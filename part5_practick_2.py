import time
user = {}
user['name'] = input('Ваше имя -->')
user['age'] = input('Ваш возраст -->')
user['height'] = input('Введите ваш рост -->')
user['favorite colour'] = input('Ваш любмый цвет -->')
user['favorite actor'] = input('Ваш любимый актер -->')
user['favorite fc'] = input('Ваш любимый футбольный клуб -->')
user['favorite game'] = input('Ваша любимая игра -->')
print('Итак. Пользователя зовут {0}, ему {1} лет, его рост - {2}. Его любимый цвет - {3}.Его любимый актер - {4}. Он болеет за {5}. Играет в {6}'.format(user['name'], user['age'], user['height'], user['favorite colour'], user['favorite actor'],
user['favorite fc'], user['favorite game']))
time.sleep(2)
print('Идет анализ пользователя...')
time.sleep(2)
if int(user['age']) < 20:
    print('{0} еще малой'.format(user['name']))
else:
    print('Пользователь стар как Бейсик') 
if user['favorite actor'] == 'Харрисон Форд':
    print('{0} шарит за Звездные Войны или Индиана Джонса'.format(user['name']))
else:
    print('Не знаю таких!')    
if user['favorite fc'] == 'Зенит':
    print('{0} разбирается в футболе'.format(user['name']))
else:
    ('Осуждаю!')
if user['favorite game'] == 'CS':
    print('Да он еще и киберспортсмен!')
else:
    print('Пользователь играет в {0}... Хороший выбор!'.format(user['favorite game']))                     