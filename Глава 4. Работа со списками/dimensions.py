# Кортежи - неизменяемые списки
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# А если попробовать поменять значение в кортеже, то получим ошибку
# dimensions[0] = 250

# Цикл for в кортеже работает так же, как и в списках
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Чтобы поменять значение в кортеже, надо полностью переопределить весь кортеж
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
