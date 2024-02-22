# Перебор всего списка - for
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)  # в начале этой строки обязательно нужен отступ

    # Сообщение с каждым элементом из списка
    magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, это был грандиозный фокус!')
    print(f'Не могу ждать, чтобы увидеть следующий трюк, {magician.title()}!\n')

print('Благодарим каждого из вас. Это было потрясающее магическое шоу!')
