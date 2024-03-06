# Чтобы сразу же прервать программу, есть команда break - она работает со связкой while True, которая всегда будет выполняться
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f'I`d love to go {city.title()}!')

# Команда break может использоваться в любых циклах, например в for