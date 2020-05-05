class C:

    num_of_sales = 0

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @staticmethod
    def say_hello(number):
        if number > 10:
            print('Welcome!')



C.say_hello()
C.say_hello()
print(C.num_of_sales)