import random


def random_numbers(num):

    start = 0

    while start < num:
        yield random.randint(0, 100)
        start += 1


# for number in random_numbers(10):
#     print(number)

# iterator = iter(random_numbers(3))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


def test_yield():
    idx = 0

    while True:
        yield idx
        print('Hello')
        yield idx
        print('World')
        idx += 1


for i in test_yield():
    print(i)

