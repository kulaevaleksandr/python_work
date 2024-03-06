# Запрашиваем данные у пользователя и сохраняем в словаре

responses = {}

# Установка флага продолжения опроса
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя.
    name = input('\nВаше имя? ')
    response = input('На какую гору вам хотелось бы подняться? ')

# Ответ сохраняется в словаре:
    responses[name] = response

# Проверка продолжения опроса.
    repeat = input('\nХотите ли дать другому человеку ответить? (Да/Нет) ')
    if repeat.lower() == 'нет':
        polling_active = False

# Опрос завершен, вывести результаты
print('\n---Результаты опроса---')
for name, response in responses.items():
    print(f'{name.title()} хочет подняться на гору {response.title()}.')


