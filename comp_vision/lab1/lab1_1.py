import math as m


def cot(x):
    return 1 / m.tan(x)


def fun(x):
    multiplier1 = m.sin(x + 5) ** (x-2) + m.tan(x - 3) ** 7 + m.log(x - 5, 10)
    multiplier2 = -x / (abs(x - cot(x)) * m.log(x))
    return -multiplier1 * multiplier2


x = None
while x is None:
    try:
        x = float(input("Введите значение x: "))
    except ValueError:
        print("Недопустимое значение")
    else:
        if not(x > 5 and m.sin(x) != 0 and x != cot(x) and m.sin(x + 5) > 0):
            print("Значение не входит в ОДЗ (x > 5; sin(x) != 0; x != cot(x)); sin(x+5) > 0")
            x = None

print(f"Значение функции в точке {x}: {fun(x):.3f}")