# Списки могут быть динамическими и изменяться по ходу выполнения программы
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Динамическое добавление элемента в конец списка - append()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# Добавление элементов аппендом в пустой список
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Добавление элемента на определённую позицию - insert(место, значение)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Удаление элемента из списка
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# Удаление элемента из списка с сохранением возможности с ним работать - pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# Удаление элемента из списка, если знаешь значение элемента
motorcycles = ['ducati', 'honda', 'yamaha', 'suzuki']
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

# Примечание: Метод remove() удаляет только первое вхождение заданного значения. Если существует вероятность того, что значение встречается в списке более одного
раза, нужно
использовать
цикл.
