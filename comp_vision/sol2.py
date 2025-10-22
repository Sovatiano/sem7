num = input()[::-1]
summ = sum([int(s) for s in num])
print(f"Перевёрнутое число: {num}")
print(f"Сумма цифр в числе: {summ}")