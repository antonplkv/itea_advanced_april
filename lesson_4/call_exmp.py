class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Decoration inside class')
        return self.func(*args, **kwargs)


def hello(name):
    return f'Hello, {name}'


r = Decorator(hello)('Anton')
print(r)