#Упорядочение элементов в списке по алфавиту - Важно! через sort() меняется порядок элементов в списке насовсем, вернуться к исходному не получится 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# В обратном порядке по алфавиту
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Временная сортировка списка функцией sorted() 
# Кстати reverse=True на эту функцию тоже работает
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Оригинальный список:")
print(cars)
print("Список в отсортированном виде:")
print(sorted(cars))
print("И снова список в оригинале:")
print(cars)

#Изменение порядка элементов в списке на обратный 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#Определение длины списка - Работает в терминале питона
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)


