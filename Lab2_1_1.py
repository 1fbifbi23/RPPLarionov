# 1. 
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

min_num = min(num1, num2, num3)

print("Минимальное число:", min_num)

# 2. 
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if 1 <= num1 <= 50:
    print(num1)
if 1 <= num2 <= 50:
    print(num2)
if 1 <= num3 <= 50:
    print(num3)

# 3. 
m = float(input("Введите вещественное число m: "))

for i in range(1, 11):
    print(i * m)

# 4.
numbers = input("Введите последовательность целых чисел: ")
sum = 0
count = 0
num = ''
i = 0

while i < len(numbers):
    if numbers[i] != ' ':
        num += numbers[i]
    else:
        sum += int(num)
        count += 1
        num = ''
    i += 1

sum += int(num)
count += 1

print("Сумма всех чисел:", sum)
print("Количество всех чисел:", count)