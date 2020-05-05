import random


def sum_(x, y):
    return x + y


my_sum = sum_
result = my_sum(1, 10)
# print(my_sum.__name__)


def perform_sum(func_sum):
    return func_sum(random.randint(10, 20), random.randint(10, 20))


result = perform_sum(sum_)
# print(result)


def a(a_):
    def b(b_):
        def c(c_):
            def d(d_):
                print(a_, b_, c_, d_)
                return True
            return d
        return c
    return b


r = a(10)(20)(30)


def decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


def outer_decorator_negative(warning=True):
    def inner_decorator_negative(func):

        def wrapper(*args, **kwargs):
            for value in list(args) + list(kwargs.values()):
                if value < 0:
                    print(f'Warning argmunets have a negative value {value}')
                    if warning == True:
                        pass
                    else:
                        return
            return func(*args, **kwargs)
        return wrapper
    return inner_decorator_negative


@outer_decorator_negative()
def div(a, b):
    return a / b


outer_decorator_negative(warning=True)(div)(100, 300)


@decorator
def make_negative(value):
    return -value


a = make_negative
print(a)
print(r)