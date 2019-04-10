# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a = float(input('Введите число 1: ', ))
b = float(input('Введите число 2: ', ))
c = float(input('Введите число 3: ', ))
if a > b and a > c:
    if b > c:
        print('Число {} среднее'.format(b))
    else:
        print('Число {} среднее'.format(c))
elif b > a and b > c:
    if a > c:
        print('Число {} среднее'.format(a))
    else:
        print('Число {} среднее'.format(c))
elif c > a and c > b:
    if a > b:
        print('Число {} среднее'.format(a))
    else:
        print('Число {} среднее'.format(b))


