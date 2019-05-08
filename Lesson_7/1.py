"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i],orig_list[i+1] = orig_list[i+1],orig_list[i]
        n += 1
    return orig_list

list1 = []
for i in range(200):
    list1.append(random.randint(-100, 100))
print('\nНесортированный массив\n')

for i in range(len(list1)):
    if len(str(list1[i])) == 3:
        print(list1[i], end=' ')
    elif len(str(list1[i])) == 2:
        print(' '+str(list1[i]), end=' ')
    else:
        print('  '+str(list1[i]), end=' ')
    if i % 20 == 0 and i != 0:
        print('\n')

bubble_sort(list1)

print('\nОтсортированный массив\n')
for i in range(len(list1)):
    if len(str(list1[i])) == 3:
        print(list1[i], end=' ')
    elif len(str(list1[i])) == 2:
        print(' '+str(list1[i]), end=' ')
    else:
        print('  '+str(list1[i]), end=' ')
    if i % 20 == 0 and i != 0:
        print('\n')

"""
Потратил кучу времени на красивый вывод. В итоге и его не доделал, и саму сортировку не оптимизировал. 
"""


