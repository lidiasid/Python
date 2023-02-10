import math
# 3. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


n = int(input("Введите степень: "))
power = 1
for i in range(n):
    print(pow(2, power))
    power += 1
    
