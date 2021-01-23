a = input('Сколько вам лет? --> ')
with open('answer.txt', 'w') as f:
    f.write(a)