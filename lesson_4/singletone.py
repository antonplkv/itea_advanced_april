class MyClass:

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        print('Already exists')
        result = super().__new__(cls)
        cls.instance = result
        return result

    def __init__(self, x, y):
        self._x = x
        self._y = y


b = MyClass(1, 2)
c = MyClass(1, 2)
d = MyClass(3, 4)

print(b is c)

