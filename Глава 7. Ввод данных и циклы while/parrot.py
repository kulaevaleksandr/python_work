# Cледующая программа предлагает пользователю ввести текст, а затем выводит сообщение для пользователя:
# message = input('Tell me something, and I will repeat it back to you: ')
# print(message)

# Добавим цикл в предыдущую программу
promt = "\nTell me something, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(promt)

    if message != 'quit':
        print(message)