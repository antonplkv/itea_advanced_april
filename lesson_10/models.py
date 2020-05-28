import mongoengine as me

me.connect('CARS')


class Cars(me.Document):
    model = me.StringField(min_length=2, max_length=64, required=True)
    engine = me.StringField(min_length=1, max_length=64, required=True)
    num_of_doors = me.IntField(min_value=1)
    colour = me.StringField(min_length=2, max_length=64)


def fill_db():
    Cars.objects.create(model='audi', engine='v8', num_of_doors=4, colour='white')
    Cars.objects.create(model='bmw', engine='v8', num_of_doors=2, colour='white')
    Cars.objects.create(model='vw', engine='v6', num_of_doors=4, colour='yellow')


if __name__ == '__main__':
    fill_db()