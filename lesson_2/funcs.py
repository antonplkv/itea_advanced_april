def my_func():
    return None


def my_sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total


a = my_sum(10, 100, 100, 12, 12)
print(a)


def my_check(**kwargs):
    print(kwargs)


my_dict = {'arg1': 12, 'arg2': 13, 'arg100': 200}

my_check(**my_dict)