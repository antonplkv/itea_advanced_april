import mongoengine as me
import datetime

me.connect('test_lesson_10')


class Author(me.Document):
    name = me.StringField(min_length=1, max_length=128)
    surname = me.StringField(min_length=1, max_length=128)

    def change_name(self, new_name):
        self.name = new_name
        self.save()

    def __str__(self):
        return f'{self.id} - {self.name}'


class Post(me.Document):
    author = me.ReferenceField(Author)
    title = me.StringField(min_length=2, max_length=256, required=True)
    body = me.StringField(min_length=2, max_length=4096, required=True)
    created = me.DateTimeField(default=datetime.datetime.now())
    marks = me.ListField()

    def __str__(self):
        return f'{self.id} - {self.title}'


if __name__ == '__main__':
    #
    # author = Author.objects.create(name='Arthur', surname='Cohnan')
    #
    # post = Post.objects.create(author=author,
    #                            title='New book',
    #                            body='Text',
    #                            marks=[5, 5, 5])
    post = Post.objects.filter(body='Text')[0]
    print(post.author.name, post.author.surname, post.author.id)
