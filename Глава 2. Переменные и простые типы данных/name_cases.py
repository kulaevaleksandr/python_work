# Вывод сообщения с переменной
name = "Максим"
message = f'Привет, {name}! Давай посмотрим что-нибудь новое. \nУкажи нужный жанр.'
print(message)

# Правка регистра
print(name.title())
print(name.lower())
print(name.upper())

# Вывод кавычек
thought = 'Народная мудрость гласит: "Не работа красит человека, а человек работу."'
print(thought)

author = "Дейл Карнеги"
quote = "Если вы ошиблись, то признавайте это быстро и решительно!"
message = f'{author} в одной из своих книг написал: {quote}'
print(message)

# Функции удаления лишних пробелов в пользовательском вводе
user = "   Василий   "
print(f'__|{user}|__')
print(f'__|{user.lstrip()}|__')
print(f'__|{user.rstrip()}|__')
print(f'__|{user.strip()}|__')