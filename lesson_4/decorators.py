#Использование декораторов внутри классов
#Реализация вне класса, отдельной функцией
#Реализация другого класса, со staticmethod декоратором
#Класс в классе

class MyClass:

    def __init__(self):
        pass

    class Decorators:

        @staticmethod
        def decorator(func):
            def wrapper(*args):
                print(args)
                func(*args)
                print('Decorated')

            return wrapper

    @Decorators.decorator
    def make_smth(self, a):
        print(f'Doing smth {a}')


MyClass().make_smth(1)

from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper(*args):
        print(args)
        func(*args)
        print('Decorated')

    return wrapper


@decorator
def target(a, b):
    print(a, b)

target.__wrapped__(10, 20)