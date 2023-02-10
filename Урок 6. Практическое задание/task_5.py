
"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    title = ()
    draw = ()

    def start(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    title = ()
    draw = ()

    def start(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    title = ()
    draw = ()

    def start(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    title = ()
    draw = ()

    def start(self):
        print('Запуск отрисовки маркером')

Pen1 = Pen()
Pencil1 = Pencil()
Handle1 = Handle()
Stationery1 = Stationery()

Stationery1.start()
Pen1.start()
Pencil1.start()
Handle1.start()



