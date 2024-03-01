# Словарь коллег и их любимых языков программирования
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages: - будет работать так же
for name in favorite_languages.keys():
    print(name.title())

# Чтобы вывести особые сообщения для нужных друзей, используем сначала цикл, а потом функцию if с условием
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f'Hi {name.title()}')
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Проверим, участвовал ли человек в опросе
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Выведем значения ключей в алфавитном порядке
for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll.')

# Перебор всех значений в словаре
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print('Были упомянуты следующие языки:')
for language in favorite_languages.values():
    print(language.title())

# Однако вывод не учитывает повторение значений
# Чтобы вывести уникальные значения, используем set
print('\nБыли упомянуты следующие языки:')
for language in set(favorite_languages.values()):
    print(language.title())

# Добавляем списки в словарях
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is {languages}.")