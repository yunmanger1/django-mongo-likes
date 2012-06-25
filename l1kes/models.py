import mongoengine as me
from mongoengine.django.auth import User as MongoUser
import datetime


class Like(me.Document):
    user = me.ReferenceField(MongoUser, required=True)
    obj = me.GenericReferenceField(required=True)
    is_enabled = me.BooleanField(required=True, default=True)
    ts = me.DateTimeField()

    def save(self, *a, **kw):
        self.ts = datetime.datetime.now()
        return super(Like, self).save(*a, **kw)


class Subscribe(me.Document):
    user = me.ReferenceField(MongoUser, required=True)
    obj = me.GenericReferenceField(required=True)
    is_enabled = me.BooleanField(required=True, default=True)
    ts = me.DateTimeField()

    def save(self, *a, **kw):
        self.ts = datetime.datetime.now()
        return super(Subscribe, self).save(*a, **kw)
