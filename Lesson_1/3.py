# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = int(input('Введите абсциссу точки 1 :',))
y1 = int(input('Введите ординату точки 1 :',))
x2 = int(input('Введите абсциссу точки 2 :',))
y2 = int(input('Введите ординату точки 2 :',))
k = str((y2 - y1) / (x2 - x1))
b = str(y1 - (((y2 - y1) / (x2 - x1)) * x1))
print(k)
print(b)
print('Данные координаты принадлежат функции: y = {} * x + {}'.format(k, b))