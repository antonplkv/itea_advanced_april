class MyClass:

    def __init__(self, num):
        self._structure = [0] * num

    def __getitem__(self, item):
        return self._structure[item]

    def __setitem__(self, key, value):
        self._structure[key] = value


obj = MyClass(10)
obj[0] = 10
print(obj[0])

for i in obj:
    print(i)