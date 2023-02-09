import random
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

numbers = []
n = int(input("Введите длину массива: "))
for i in range(n):
    numbers.append(random.randrange(1, 10))
print(numbers)    

x = int(input("Введите искомое число: "))
a = 0
for i in range(len(numbers)):
    if numbers[i] == x:
        a += 1
print(a)             
    