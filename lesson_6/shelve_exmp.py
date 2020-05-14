import shelve

filename = 'MyShelveDb'


# def add_user(username):
#
#     with shelve.open(filename) as db:
#
#         users = db.get('users', default=[])
#         users.append(username)
#         db['users'] = users
#
#
# def get_users():
#
#     with shelve.open(filename) as db:
#         return db.get('users', default=[])
#
# def get_iter():
#     with shelve.open(filename) as db:
#         for k in db:
#             print(k)



def add_user(username, id):
    with shelve.open(filename) as db:
        db['users'] = {''}
        print(db['users'][id])


add_user('123', 1)