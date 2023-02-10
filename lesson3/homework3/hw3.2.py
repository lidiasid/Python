import random
# 2 Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

numbers = []
n = int(input("Введите длину массива: "))
for i in range(n):
    numbers.append(random.randrange(1, 10))
print(numbers)    

x = int(input("Введите число: "))
closest = None
for i in range(len(numbers)):
    if closest is None or abs(numbers[i] - x) < abs(closest - x):
        closest = numbers[i]
print(closest)