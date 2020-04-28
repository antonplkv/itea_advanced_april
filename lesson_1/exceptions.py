try:
    var2 = 1 / 0
except (ZeroDivisionError, TypeError):
    var2 = None
except (KeyboardInterrupt):
    print('1')

print(var2)