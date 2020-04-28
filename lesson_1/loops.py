i = 0
while i < 20:
    i += 1

    if i == 10:
        break
    print(f'Hello {i}')

else:
    print('Succesfuly')


for idx, value in enumerate([1, 2, 6, 3]):
    print(f'The index is {idx}, the value {value}')