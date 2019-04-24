# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

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
    cifra1 = chislo // 100
    cifra2 = (chislo // 10) % 10
    cifra3 = chislo % 10
    print('Сумма цифр числа: ', cifra1 + cifra2 + cifra3)
    print('Произведение цифр числа: ', cifra1 * cifra2 * cifra3)

# print(timeit.timeit('func1(chislo)'))
# print(timeit.timeit('func2(chislo)'))

cProfile.run(func1(chislo))

# Код я написал, но работать он не хочет, а времени разобраться к сожалению нет. :(




