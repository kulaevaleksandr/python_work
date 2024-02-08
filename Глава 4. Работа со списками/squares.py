# Создание списка квадратов чисел от 1 до 10 
squares = []
for value in range(1,11):
 square = value**2
 squares.append(square)
print(squares)

#То же самое, но с небольшим сокращением
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

# Генератор списка, выполняющий то же, что и оба варианта выше
squares = [value**2 for value in range(1,11)]
print(squares)

#Упражнения
numbers = list(range(1,21))
print(numbers)


