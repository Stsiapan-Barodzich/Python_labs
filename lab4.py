from math import sin, sqrt
import matplotlib.pyplot as plt
import numpy as np

# Определяем f(x) = x^2
def f(x):
    return x ** 2

# Функция c(x, y) из первого уравнения
def c(x, y):
    if x - y == 0:
        return (f(x)**2 + y**2 + sin(y))
    elif x - y > 0:
        return ((f(x) - y)**2 + np.cos(y))
    else:  # x - y < 0
        return ((y - f(x))**2 + np.tan(y))

# Функция a(x, y) из второго уравнения
def a(x, y):
    if x * y > 0:
        sqrt_term = sqrt(max(f(x) * y, 0))  # Защита от отрицательных значений под корнем
        return (f(x) + y)**2 - sqrt_term
    elif x * y < 0:
        return (f(x) + y)**2 + sqrt(abs(f(x) * y))
    else:  # x * y == 0
        return (f(x) + y)**2 + 1

# Построение графиков функций c(x, y) и a(x, y)
def plot_functions():
    x = np.linspace(-5, 5, 200)
    y = np.linspace(-5, 5, 200)
    x, y = np.meshgrid(x, y)

    # Вычисляем значения функций
    z_c = np.vectorize(c)(x, y)
    z_a = np.vectorize(a)(x, y)

    # Создаем график
    fig = plt.figure(figsize=(12, 6))

    # График для c(x, y)
    ax1 = fig.add_subplot(121, projection='3d')
    surf1 = ax1.plot_surface(x, y, z_c, cmap='viridis')
    ax1.set_title("График функции c(x, y) (Вариант 3)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_zlabel("c(x, y)")
    fig.colorbar(surf1, ax=ax1)

    # График для a(x, y)
    ax2 = fig.add_subplot(122, projection='3d')
    surf2 = ax2.plot_surface(x, y, z_a, cmap='plasma')
    ax2.set_title("График функции a(x, y) (Вариант 1)")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_zlabel("a(x, y)")
    fig.colorbar(surf2, ax=ax2)

    plt.tight_layout()
    plt.show()

# Вызываем построение графиков
if __name__ == "__main__":
    plot_functions()
