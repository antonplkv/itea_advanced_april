
try:
    number = int(input('Enter the number'))
except ValueError as exc:
    print(exc)
    print('Value must be a number')
    number = 0
else:
    print('The data is correct.')
finally:
    print('Thank you!')


print(number ** 2)
