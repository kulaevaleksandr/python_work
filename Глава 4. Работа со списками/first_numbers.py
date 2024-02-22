# Вывод числовой последовательности - range()
for value in range(1, 5):
    print(value)

# Но снова идёт смещение на 1, поэтому чтобы вывести цифры до 5, нужно делать так:
for value in range(1, 6):
    print(value)

# Можно задать вывод чисел с 0
for value in range(6):
    print(value)
