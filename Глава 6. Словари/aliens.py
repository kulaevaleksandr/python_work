# Вложения: словари в списке, списки в словарях и дае словари в словарях
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Создание пустого списка для хранения пришельцев
aliens = []

# Создание 30 зелёных пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Поменяем первых трёх пришельцев зелёных на жёлтых
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# а если какие-то пришельцы в первых трёх уже жёлтые, то меняем их на красные
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Вывод первых 5 пришельцев
for alien in aliens[:5]:
    print(alien)
print('...')

# Вывод количества созданных пришельцев
print(f'\nTotal number of aliens: {len(aliens)}')