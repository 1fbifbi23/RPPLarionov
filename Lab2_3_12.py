import sys
import random

# 1. Считываем массив из параметров командной строки
A = []
for i in range(10):
    elem = int(input("Введите элемент массива A: "))
    A.append(elem)

# 2. Находим наименьший нечетный элемент
min_odd = None
for num in A:
    if num % 2 != 0:
        if min_odd is None or num < min_odd:
            min_odd = num

if min_odd is not None:
    print(f"Наименьший нечетный элемент массива A: {min_odd}")
else:
    print("В массиве A нет нечетных элементов")

# 3. Создаем массив B со случайными элементами
B = [random.randint(0, 100) for _ in range(10)]

# 4. Меняем местами элементы массивов A и B
A, B = B, A

# 5. Выводим массивы A и B
print("Массив A после замены с B:", A)
print("Массив B после замены с A:", B)