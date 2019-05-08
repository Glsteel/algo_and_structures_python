"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from memory_profiler import profile

@profile
def func1(chislo):
# chislo = input('Введите трехзначное число: ', )
    cifra1 = int(chislo[0])
    cifra2 = int(chislo[1])
    cifra3 = int(chislo[2])
    a = cifra1 + cifra2 + cifra3
    b = cifra1 * cifra2 * cifra3
    print('Сумма цифр числа: ', a)
    print('Произведение цифр числа: ', b)
    return a, b

@profile
def func2(chislo):
# chislo = int(input('Введите трехзначное число: ', ))
    cifra1 = int(chislo) // 100
    cifra2 = (int(chislo) // 10) % 10
    cifra3 = int(chislo) % 10
    print('Сумма цифр числа: ', cifra1 + cifra2 + cifra3)
    print('Произведение цифр числа: ', cifra1 * cifra2 * cifra3)

chislo = '123'
func1(chislo)
func2(chislo)



"""
Оба примера выполняются одновременно, оба не дают никаких сколь либо ощутимых результатов. :)
Win 64, Python 3.7

Line #    Mem usage    Increment   Line Contents
================================================
    13     13.2 MiB     13.2 MiB   @profile
    14                             def func1(chislo):
    15                             # chislo = input('Введите трехзначное число: ', )
    16     13.2 MiB      0.0 MiB       cifra1 = int(chislo[0])
    17     13.2 MiB      0.0 MiB       cifra2 = int(chislo[1])
    18     13.2 MiB      0.0 MiB       cifra3 = int(chislo[2])
    19     13.2 MiB      0.0 MiB       a = cifra1 + cifra2 + cifra3
    20     13.2 MiB      0.0 MiB       b = cifra1 * cifra2 * cifra3
    21     13.2 MiB      0.0 MiB       print('Сумма цифр числа: ', a)
    22     13.2 MiB      0.0 MiB       print('Произведение цифр числа: ', b)
    23     13.2 MiB      0.0 MiB       return a, b

Сумма цифр числа:  6
Произведение цифр числа:  6

Filename: C:/Users/K501/Desktop/Pyton/Программы/algo_and_structures_python/Lesson_6/1.1.py

Line #    Mem usage    Increment   Line Contents
================================================
    25     13.3 MiB     13.3 MiB   @profile
    26                             def func2(chislo):
    27                             # chislo = int(input('Введите трехзначное число: ', ))
    28     13.3 MiB      0.0 MiB       cifra1 = int(chislo) // 100
    29     13.3 MiB      0.0 MiB       cifra2 = (int(chislo) // 10) % 10
    30     13.3 MiB      0.0 MiB       cifra3 = int(chislo) % 10
    31     13.3 MiB      0.0 MiB       print('Сумма цифр числа: ', cifra1 + cifra2 + cifra3)
    32     13.3 MiB      0.0 MiB       print('Произведение цифр числа: ', cifra1 * cifra2 * cifra3)
"""
