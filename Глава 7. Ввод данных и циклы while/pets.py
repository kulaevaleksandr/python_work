# Используем remove() в связке с while, чтобы удалить все повторяющиеся значения в списке
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
