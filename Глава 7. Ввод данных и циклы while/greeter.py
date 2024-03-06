name = input('Please enter your name: ')
print(f'\nHello, {name}')

# Иногда подсказка бывает оч большой, поэтому можно создать переменную с подсказкой и использовать её

promt = 'If you tell us who you are, we can personalize the messages you see.'
promt += '\nWhat is your first name? '

name = input(promt)
print(f'Hello, {name}!')

# Когда пользователь вводит число, интерпретатор понимает это как строку и сравнить с другими числами не может
# Чтобы это сделать, нужно использовать функцию int
age = input('How old are you? ')
age = int(age)
age >= 18