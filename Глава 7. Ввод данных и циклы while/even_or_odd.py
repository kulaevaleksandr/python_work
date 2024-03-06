# Проверим, чётные ли числа
number = input('Введи число, чтобы проверить, чётное оно или нет: ')
number = int(number)

if number % 2 == 0:
    print(f'\nЧисло {number} - чётное.')
else:
    print(f'\nЧисло {number} - нечётное.')