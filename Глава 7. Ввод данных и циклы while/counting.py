# цикл while можно использовать для перебора числовой последовательности
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Команда continue возвращает к началу циклу и проверке условия

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# У каждого цикла while должна быть возможность заверщения, чтобы цикл не выполнялся бесконечно
x = 1
while x <= 5:
    print(x)
    x += 1

# бесконечный цикл! - выдаёт бесконечную серию единиц
# x = 1
# while x <= 5:
#     print(x)


