import math

def calculate_c(x, y):
    if x - y == 0:
        c = x**4 + y**2 + math.sin(y)  # f(x) = x^2, поэтому f(x)^2 = x^4
    elif x - y > 0:
        c = (x**2 - y)**2 + math.cos(y)  # f(x) = x^2
    else:  # x - y < 0
        c = (y - x**2)**2 + math.tan(y)  # f(x) = x^2
    return c

# Ввод значений
x = float(input("Введите x: "))
y = float(input("Введите y: "))

# Вычисление c
result = calculate_c(x, y)
print(f"Результат: c = {result}")
