import csv

arr = [['Звездные войны', 'Терминатор', 'Искусственный интелект'], ['Дурак', 'Матильда', 'Левиафан'], ['Люди в черном', 'Я - робот', 'Эволюция']]
with open('films.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(arr[0])
    w.writerow(arr[1])
    w.writerow(arr[2])
    