

# def main(a, b):
#     return a + b
#
#
# def start():
#     print('hello world')
#
#
# main(start)


# source_list = [2, 4, 8]
# squares_list = []
#
# for num in source_list:
#     squares_list.append(num ** 2)


#l = map(lambda a, b: (a ** 2, b ** 2), [2, 4, 8], [6, 7, 8])

import random

my_list = [random.randint(0, 100) for _ in range(100)]

result = filter(lambda elem: elem < 10, my_list)
print(list(result))


#zip_longest

res = zip([1, 2, 3], [2, 3, 4])
print(dict(res))