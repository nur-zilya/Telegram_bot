from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('test.db')


class ModelBase(db.Model):
    created_at = pw.DateTimeField(default=datetime.now())

    class Meta():

        database = db


class History(ModelBase):
    number = pw.TextField()
    message = pw.TextField()

