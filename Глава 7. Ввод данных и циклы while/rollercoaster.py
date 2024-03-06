# Проверим, подходит ли рост для катания на аттракционе
height = input('How tall are you, in iches? ')
height = int(height)
if height >= 48:
    print('\nYou`re are tall enough to ride!')
else:
    print('\nYou`ll be able to ride when you`re a little older.')
