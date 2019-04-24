"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import timeit
import cProfile

chislo = '123'

def func1 (chislo):
    # chislo = input('Введите трехзначное число: ', )
    cifra1 = int(chislo[0])
    cifra2 = int(chislo[1])
    cifra3 = int(chislo[2])
    print('Сумма цифр числа: ', cifra1 + cifra2 + cifra3)
    print('Произведение цифр числа: ', cifra1 * cifra2 * cifra3)

def func2 (chislo):
    # chislo = int(input('Введите трехзначное число: ', ))
    chislo = int(chislo)
    cifra1 = chislo // 100
    cifra2 = (chislo // 10) % 10
    cifra3 = chislo % 10
    print('Сумма цифр числа: ', cifra1 + cifra2 + cifra3)
    print('Произведение цифр числа: ', cifra1 * cifra2 * cifra3)

cProfile.run(func1(chislo))
cProfile.run(func2(chislo))


