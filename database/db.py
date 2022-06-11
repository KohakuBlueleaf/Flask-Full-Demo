from mongoengine import *
from pymongo import MongoClient as Client


# Ensure Your MongoDB is running!
DB_URI = 'mongodb://localhost:27017/test_chat'
client = Client(host=DB_URI)
client.test.command("ping")
connect(host=DB_URI)


class UserDB(Document):
    name = StringField()
    pswd = StringField()


class MessageDB(Document):
    author = ReferenceField(UserDB)
    content = BinaryField()
    time = IntField()
