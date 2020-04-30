class Cat:

    def __init__(self, name, gender):
        self._name = name
        self._gender = gender

    def meow(self):
        print(f'{self._name} says Meow')

    def __eq__(self, other):
        return self._name == other._name and self._gender == other._gender

    def __add__(self, other):
        new_cat = Cat(name=self._name + other._name, gender=self._gender)
        return new_cat

    def __str__(self):
        return self._name


cat1 = Cat('Jack', 'male')
cat2 = Cat('Linda', 'female')

cat1.meow()
cat2.meow()

print(cat1 == cat2)
print(cat1.__eq__(cat2))

print(cat2 + cat1 + cat1)