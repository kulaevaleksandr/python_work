vehicle = ['Авто', 'Мотоцикл', 'Трамвай', 'Поезд', 'Самолёт', 'Корабль']
print(vehicle[0])
print(vehicle[1].lower())
print(vehicle[-1])

message = f'Самый быстрый транспорт - это {vehicle[-2].lower()}.'
print(message)

vehicle[1] = 'Автобус'
print(vehicle)

vehicle.append('Катер')
print(vehicle)

vehicle.insert(0, 'Вертолёт')
print(vehicle)

del vehicle[-2]
print(vehicle)

popped_vehicle = vehicle.pop(1)
print(popped_vehicle)
print(vehicle)

vehicle.remove('Трамвай')
print(vehicle)

print(sorted(vehicle))
print(sorted(vehicle, reverse=True))
print(vehicle)
vehicle.reverse()
print(vehicle)
vehicle.sort()
print(vehicle)
vehicle.sort(reverse=True)
print(vehicle)

