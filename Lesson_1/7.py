"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

storona1 = int(input('Введите длину стороны 1: ', ))
storona2 = int(input('Введите длину стороны 2: ', ))
storona3 = int(input('Введите длину стороны 3: ', ))
if (storona1 + storona2) > storona3 and(storona1 + storona3) > storona2 and (storona2 + storona3) > storona1:
    print('Такой треугольник существует')
    if storona1 == storona2 and storona1 == storona3:
        print('Треугольник является равносторонним')
    elif storona1 == storona2 or storona1 == storona3 or storona2 == storona3:
        print('Треугольник является равнобедренным')
else:
    print('Такого треугольника не существует')

