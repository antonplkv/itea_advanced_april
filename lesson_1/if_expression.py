temperature = 25
weather_type = 'Sunny'

if temperature > 20 and weather_type == 'Sunny':
    print('hot')
elif temperature > 15:
    print('worm')
elif temperature < 0:
    print('cold')
else:
    print('The weather is okay')


result = 'Hot' if temperature > 20 else 'Not hot'
print(result)

my_var = None

if my_var:
    print('SALUT')