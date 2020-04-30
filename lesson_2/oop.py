class Phone:
    description = 'The class for phone'

    def __init__(self, model, imei):
        self._model = model
        self._imei = imei

    def get_model(self):
        return self._model

    def set_model(self, value):
        self._model = value

    def get_imei(self):
        return self._imei

    def set_imei(self, value):
        self._imei = value

    def call(self):
        print(f'Making call from {self._model}...')


class MobilePhone(Phone):

    def send_message(self):
        print(f'Sending message from {self._model}...')

    def call(self):
        print(f'Making call from MobilePhone')

Phone.description = 'New description'
phone = Phone('Nokia', '12312')
phone.call()

phone2 = MobilePhone('Samsung', 'eqewqeqweqw')
phone2.call()


phone2.description = 'Samsung phone'
print(phone2.description)
print(phone.description)
#Acces to class variable

