list_of_squares = []

for number in range(0, 10):
    list_of_squares.append(number ** 2)
print(list_of_squares)

list_of_squares_comprehension = [number ** 2 if number % 2 else number ** 3 for number in range(0, 10)]
set_of_squares_comprehension = {number ** 2 if number % 2 else number ** 3 for number in range(0, 10)}

print(list_of_squares_comprehension)
print(set_of_squares_comprehension)


base = [(1, 2, 4), (2, 4, 8), (5, 10, 20)]

dict_compr = {b[0]: (b[1], b[2]) for b in base}
print(dict_compr)

tuple_of_squares_comprehension = (number ** 2 if number % 2 else number ** 3 for number in range(0, 10))
print(tuple(tuple_of_squares_comprehension))