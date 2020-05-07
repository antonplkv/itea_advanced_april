# class MyException(Exception):
#     pass
#
#
# def main(a, b):
#     if a == 0:
#         raise MyException('Cannot pass 0 in this case!!!!')
#
# main(0, 1)


import abc


class AbstractCar(abc.ABC):

    @abc.abstractmethod
    def move(self):
        pass

    @abc.abstractmethod
    def open_door(self):
        print('Openning door')


class Car(AbstractCar):

    def __init__(self):
        pass

    def open_door(self):
        super().open_door()


Car().move()
