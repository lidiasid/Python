# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

a = list(map(int, input("Введите первый массив: ").split()))
b = list(map(int, input("Введите второй массив: ").split()))

print([item for item in a if item not in b])
