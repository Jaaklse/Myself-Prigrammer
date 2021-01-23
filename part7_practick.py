numbers = [32, 12, 9, 67, 54, 99, 88, 0, 76, 43]
print('Отгадайте число от 0 до 100!')
total_sum = 0
while True:
    try:
        a = input('Ваше число? -->')
        if a == 'X':
            print('Всего вы заработали {0}$'.format(total_sum))
            break
        else:
            a = int(a)
            if a in numbers:
                print('Поздравляю! Вы отгадали! На ваш счет зачислено 100$')
                total_sum += 100
                print('Ваш текущий счет составляет {0}$!'.format(total_sum))
            else:
                print('К сожалению, вы не отгадали... Попробуйте еще раз!') 
    except ValueError:
        print('Эм... Вы ввели букву вместо цифры')        
         