# В переменной хранится заказанный топпинг к пицце; если клиент не заказал анчоусы (anchovies), программа выводит сообщение:
requested_topping = 'mushrooms'
# Проверяем неравенство
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Чтобы узнать, присутствует ли заданное значение в списке, воспользуйтесь ключевым словом in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
# True

'pepperoni' in requested_toppings
# False

# Чтобы проверить каждый элемент под условия, не используем elif и else, а каждый пропускаем через if
requested_toppings = ['грибы', 'больше сыра']
if 'грибы' in requested_toppings:
    print("Добавлены грибы.")
if 'пепперони' in requested_toppings:
    print("Добавлено пепперони.")
if 'больше сыра' in requested_toppings:
    print("Добавлено больше сыра.")

    print("\nВаша неповторимая пицца готова!")

# Можно оптимизировать код с помощью цикла
requested_toppings = ['грибы', 'халапеньо', 'больше сыра']
for requested_topping in requested_toppings:
    print(f"Добавлено: {requested_topping}.")
print("\nВаша неповторимая пицца готова!")

# А если закончился ингридиент, можно вывести сообщение об этом
requested_toppings = ['грибы', 'халапеньо', 'больше сыра']
for requested_topping in requested_toppings:
    if requested_topping == 'грибы':
        print(f"Извините. Увы, {requested_topping} не добавить. Этого пока что нет.")
    else:
        print(f"Добавлено: {requested_topping}.")
print("\nВаша неповторимая пицца готова!")

# Списки могут быть пустыми. Вот как с ними можно работать:
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Добавили {requested_topping}.")
    print("\nВаша неповторимая пицца готова!")
else:
    print("Вы хотите пиццу без топпингов?")
# Гость хочет добавить топпинги. Есть два списка: доступные топпинги и желаемые гостем
available_toppings = ['грибы', 'оливки', 'халапеньо',
                      'пепперони', 'ананас', 'больше сыра']

requested_toppings = ['грибы', 'фри', 'больше сыра']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Добавили {requested_topping}.")
    else:
        print(f"Извините, не можем добавить {requested_topping}. У нас этого нет.")

print("\nВаша неповторимая пицца готова!")
