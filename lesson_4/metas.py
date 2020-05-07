# obj_int = 11
#
# print(isinstance(obj_int, (int, str)))
#
# print(type(obj_int))
#
#
# class C:
#     pass
#
#
# a = C
#
# print(type(type(C)))
#
#
# def my_method(self):
#     self._object_var = 123
#
#
# my_class = type(
#     'MyClass',
#     (),
#     {'class_attr': 123, 'qwe': 345, 'my_method': my_method}
#
# )
#
# print(my_class.__name__)
# obj = my_class()
# obj.my_method()
# print(obj._object_var)


class MyMixin:

    def test(self):
        print('1223')

    def test_w(self):
        pass


class MyMetaClass(type):

    def __new__(cls, name, bases, attrs):
        # if '_' in name:
        #     print('ERROR!')
        #     return None
        new_class = super().__new__(cls, name, (MyMixin, ), attrs)
        return new_class


class My_Class(metaclass=MyMetaClass):

    description = 'This class for test metaclasses'

    def __init__(self, x, y):
        self._x = x
        self._y = y


My_Class(1, 2).test()