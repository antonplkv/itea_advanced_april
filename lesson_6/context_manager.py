file = open('file', mode='w')
try:
    file.write('eqwewqweq')
except IOError:
    print('Exception handled')
finally:
    file.close()


with open('test', mode='w') as file:
    file.write('qwerqweqw')


class MyContextManager:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)

        if exc_type == ZeroDivisionError:
            print('Zero division was detected')
        self._x, self._y = 0, 0


# obj = MyContextManager(10, 20)
# pass
# obj._x = 0
# obj._y = 0


with MyContextManager(10, 23) as obj:
    1 / 0
    print(obj._x, obj._y)

print(obj._x, obj._y)




