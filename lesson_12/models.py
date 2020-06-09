import mongoengine as me

me.connect('test_images')


class Gallery(me.Document):
    title = me.StringField(min_length=0, max_length=512)
    image = me.FileField()


if __name__ == '__main__':

    #SAVE
    # with open('qwe.jpeg', 'rb') as image:
    #     photo = Gallery(title='photo')
    #     photo.image.put(image, content_type='image/jpeg')
    #     photo.save()

    #READ
    # image = Gallery.objects.get(title='photo')
    # res = image.image.read()
    #
    # with open('newimage.jpeg', 'wb') as file:
    #     file.write(res)

    #Deletion
    image = Gallery.objects.get(title='photo')

    image.image.delete()
    image.save()