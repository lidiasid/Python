# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))

def Degre (a, b):

    if (b == 0):
         return 1
    return Degre (a, b-1)*a

print(Degre(a, b))



