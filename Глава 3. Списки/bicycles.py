# Вывод списка целиком в дурацком виде
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Вывод элемента из списка с выбранным индексом, в данном случае с 0
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

# Кстати индексы в списках начинаются с 0. С этим внимательней!

# Правка регистра в выводе из списка тоже работает)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

# Можно вывести несколько элементов из списка
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

# Вывод последнего элемента из списка
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

# Кстати индекс -2 выдаст второй элемент от конца списка, -3 выдаст третий и т.д.

# Составляем предложение с элементом из списка
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f'Моим первым великом был {bicycles[0].title()} синего цвета.'
print(message)
