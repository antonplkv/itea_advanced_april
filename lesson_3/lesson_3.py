class Vehicle:

    def __init__(self, model, engine):
        self._model = model
        self._engine = engine

    def move(self):
        for i in range(10):
            print('Moving')

    def __str__(self):
        return self._model


class Car(Vehicle):

    def __init__(self, model, engine, num_of_doors):
        super().__init__(model, engine)
        self.num_of_doors = num_of_doors

    def move(self):
        print('More faster')
        super().move()
        print('Moving fast')


car = Car('BMW', 'V-6')
car.move()