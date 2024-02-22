# Словарь в языке Python представляет собой совокупность пар «ключ-значение»
# В словаре alien_0 хранятся два атрибута: цвет (color) и количество очков (points).
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Пример: если игрок сбивает корабль пришельцев, то вывод сообщения может выглядеть так
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"Вы заработали {new_points} очков!")

# Зададим координаты пришельцу
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Создадим пустой словарь, а затем добавим пары ключ-значение
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Изменение значения в словаре аналогично добавлению по синтаксису
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Пример с отслеживанием координат пришельца при перемещении
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Пришелец перемещается вправо.
# Вычисляем величину смещения на основании заданной скорости.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# Пришелец двигается быстро.
    x_increment = 3
# Новая позиция равна сумме старой позиции и приращения.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Чтобы удалить пару ключ-значение из словаря используем del
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)