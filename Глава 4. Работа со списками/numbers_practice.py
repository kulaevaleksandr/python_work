# Упражнение: вывести нечётные числа от 1 до 20
numbers = list(range(1,21,2))
for number in numbers:
	print(number)

#Список чисел, кратных 3
numbers = list(range(3,30,3))
for number in numbers:
	print(number)

#Список кубов от 1 до 10 и вывод каждого в цикле
squares = []
for value in range(1,11):
 square = value**3
 squares.append(square)
 print(square)

#Генератор кубов
squares = [value**3 for value in range(1,11)]
print(squares)