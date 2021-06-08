from tinydb import TinyDB
db = TinyDB('db.json')


def insert():
    db.insert({'nik': "1"})
    db.insert({'nik': "2"})
    db.insert({'nik': "3"})


db.truncate()
insert()

print(db.all)
