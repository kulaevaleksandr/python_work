age = 24
if age < 4:
    print("Для вас вход бесплатный.")
elif age < 18:
    print("Стоимость билета для вас $25.")
else:
    print("Стоимость билета для вас $40.")

# Можно оптимизировать код вот так:
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Стоимость билета для вас ${price}.")

# Блоков elif может быть сколь угодно:
age = 63
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Стоимость билета для вас ${price}.")

# Не обязательно заканчивать блок условий функцией else. Если это удобно, можно использовать elif
age = 68
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Стоимость билета для вас ${price}.")

# Но важно, что если одно из условий подходит, то остальные просто пропускаются.