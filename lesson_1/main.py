my_list = [1, 2, 3, 4, 'zxc']
print(my_list[0])
my_list[0] = 2
print(my_list[0])
my_list.append(12)

print(my_list[5])

my_list.extend([5, 6, 7])
print(my_list)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)


products = {
    'milk': 25,
    'fish': 60,
    'tomato': 20,
    ('apple', 'potato'): 45

}

value = products.get('Gum', 'Нет элемента')
print(value)
print(products)
print(products[('apple', 'potato')])


my_set_products = {'milk', 'tomato', 'tomato', 'potato', 'fish'}
my_set_products2 = {'milk', 'spaghetti', 'cucumber', 'potato'}
print(my_set_products2.difference(my_set_products))


new_dictionary = dict(
    America='dodge',
    Germany=['Volkwsagen', 'BMW']
)
print(new_dictionary)