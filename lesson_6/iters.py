"""
>>> my_list = [1, 2, 3, 4]
>>> my_list
[1, 2, 3, 4]
>>> for i in my_list:
...     print(i)
...
1
2
3
4
>>> iterator = iter(my_list)
>>> next(iterator)
1
>>> next(iterator)
2
>>> next(iterator)
3
>>> next(iterator)
4
>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>

"""


class MyRange:

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self._start == self._end:
            raise StopIteration
        start = self._start
        self._start += 1
        return start

    def __str__(self):
        return f'MyRange({self._start}, {self._end})'


obj = MyRange(0, 5)
print(obj)

for i in obj:
    print(i)


import random


class Randomizer:

    def __init__(self, num, start_range, end_range):
        self._start = 0
        self._end = num
        self._start_range = start_range
        self._end_range = end_range

    def __iter__(self):
        return self

    def __next__(self):
        if self._start == self._end:
            raise StopIteration
        self._start += 1
        return random.randint(self._start_range, self._end_range)

# def to_square(number):
#     return number ** 2
#
# print(list(map(to_square, [1, 2, 3, 4, 5])))

rand = Randomizer(100, 300, 1000)
print(rand)

print(tuple(rand))