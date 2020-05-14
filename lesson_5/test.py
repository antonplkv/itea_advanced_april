import requests

import uuid

print(uuid.uuid4())

print(requests.get('https://classroom.google.com/u/1/c/OTA3NDYwODUxOTha').text)


open('/home/anton/itea_adv_april/lesson_4/qwe.txt', 'w')