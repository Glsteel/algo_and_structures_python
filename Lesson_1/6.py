# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

bukva = int(input('Введите порядковый номер буквы английского алфавита: ', ))
print('Введенный номер принадлежит букве {}'.format(chr(bukva + 96)))