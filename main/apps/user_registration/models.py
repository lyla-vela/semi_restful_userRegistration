from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 0:
            errors["first_name"] = " should not be empty"
        if len(postData['last_name']) < 0:
            errors["last_name"] = " should not be empty"
        if len(postData['email']) < 0:
            errors["email"] = " should not be empty"
        return errors
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True , null=True)
    def __repr__(self):
        return "<users object: {} {}>".format(self.first_name, self.last_name)
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    objects = UsersManager()