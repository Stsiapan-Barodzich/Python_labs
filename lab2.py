# Простые числа от 1 до N
def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Найти длину самой короткой строки в списке строк
def shortest_string_length(strings):
    return min(len(s) for s in strings)

# Создать множества чётных и нечётных чисел, найти пересечение
def even_odd_intersection(numbers):
    even = {num for num in numbers if num % 2 == 0}
    odd = {num for num in numbers if num % 2 != 0}
    return even & odd

# Вычислить факториал числа N с помощью цикла for
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Найти сумму всех положительных чисел в списке
def sum_positive_numbers(numbers):
    return sum(num for num in numbers if num > 0)

# Удалить все элементы, повторяющиеся более одного раза в списке
def remove_duplicates(lst):
    return [x for x in lst if lst.count(x) == 1]

# Генерировать словарь с ключами-числами от 1 до N и их обратными значениями
def generate_inverted_dict(n):
    return {i: 1 / i for i in range(1, n + 1)}

# Найти строку с наибольшим количеством символов 'a'
def string_with_max_a(strings):
    return max(strings, key=lambda s: s.count('a'))

# Объединить два словаря в один
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

# Найти сумму всех нечётных чисел от 1 до N
def sum_odd_numbers(n):
    return sum(num for num in range(1, n + 1) if num % 2 != 0)

# Примеры вызова функций
if __name__ == "__main__":
    # Простые числа
    n = int(input("Введите N для поиска простых чисел: "))
    print("Простые числа:", find_primes(n))

    # Самая короткая строка
    strings = input("Введите строки через пробел: ").split()
    print("Длина самой короткой строки:", shortest_string_length(strings))

    # Пересечение чётных и нечётных
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    print("Пересечение чётных и нечётных:", even_odd_intersection(numbers))

    # Факториал
    n = int(input("Введите число для вычисления факториала: "))
    print("Факториал:", factorial(n))

    # Сумма положительных чисел
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    print("Сумма положительных чисел:", sum_positive_numbers(numbers))

    # Удаление повторяющихся элементов
    lst = input("Введите элементы списка через пробел: ").split()
    print("Список без повторяющихся элементов:", remove_duplicates(lst))

    # Генерация словаря
    n = int(input("Введите N для генерации словаря: "))
    print("Словарь:", generate_inverted_dict(n))

    # Строка с максимальным количеством 'a'
    strings = input("Введите строки через пробел: ").split()
    print("Строка с максимальным количеством 'a':", string_with_max_a(strings))

    # Объединение двух словарей
    dict1 = {1: "a", 2: "b"}
    dict2 = {2: "c", 3: "d"}
    print("Объединённый словарь:", merge_dicts(dict1, dict2))

    # Сумма нечётных чисел
    n = int(input("Введите N для суммы нечётных чисел: "))
    print("Сумма нечётных чисел:", sum_odd_numbers(n))
