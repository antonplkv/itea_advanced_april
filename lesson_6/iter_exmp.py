class MyRangeIterator:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __next__(self):
        if self._start == self._end:
            raise StopIteration
        start = self._start
        self._start += 1
        return start


class MyRange:

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __iter__(self):
        return MyRangeIterator(self._start, self._end)

    def __str__(self):
        return f'MyRange({self._start}, {self._end})'


obj = MyRange(0, 3)

iterator = iter(obj)
print(next(iterator))
print(next(iterator))
print(next(iterator))