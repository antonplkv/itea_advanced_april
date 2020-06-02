import mongoengine as me

me.connect('lesson_11_test')


class Car(me.Document):
    model = me.StringField()
    engine = me.StringField()


class User(me.Document):

    login = me.StringField(unique=True, required=True)
    password = me.StringField(required=True, min_length=8)
    interests = me.ListField(me.StringField())
    car = me.ReferenceField(Car)


if __name__ == '__main__':
    car = Car(model='BMW', engine='V-6').save()
    User(login='qwerty123231', car=car, password='passwd1231231231', interests=['Sport', 'Books']).save()
