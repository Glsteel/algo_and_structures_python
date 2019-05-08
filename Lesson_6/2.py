"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof

class Person:
    def __init__(self, name, health, armor, damage):
        self._name = name
        self._health = health
        self._armor = armor
        self._damage = damage

class PersonSlots:
    __slots__ = ['name', 'health', 'armor', 'damage']
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self_damage = damage

player = Person('Gleb', 100, 2, 10)
print(player.__dict__)
print('\nПотребление памяти player: ', asizeof.asizeof(player))

player_sl = PersonSlots('Hleb', 200, 3, 20)
print('\nПотребление памяти player_sl: ', asizeof.asizeof(player_sl))



