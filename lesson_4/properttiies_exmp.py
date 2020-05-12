class A:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def set_a(self, value):
        if value < 0:
            raise ValueError('Value must be greater than 0')
        self._a = value

    a = property(get_a, set_a)

    # @property
    # def a(self):
    #     return self._a
    #
    # @a.setter
    # def a(self, value):
    #     if value < 0:
    #         raise ValueError('Value must be greater than 0')
    #     self._a = value

obj = A(1, 2)

# obj.get_a()
#
# obj.set_a('312312')
obj.a = -1

print(obj.abc)
