from django.db import models
from django.contrib.auth.models import User

class PetUser(models.Model):
    auth_user = models.OneToOneField(User)
    money = models.IntegerField()


class Connection(models.Model):
    user_a = models.OneToOneField(User, related_name='user_a')
    user_b = models.OneToOneField(User, related_name='user_b')


class Pet(models.Model):
    auth_user = models.ForeignKey(Connection)
    type = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    exp = models.IntegerField()


# 1 for cbt and 2 for geo
class Activity(models.Model):
    title = models.CharField(max_length=500, default="")
    description = models.CharField(max_length=500)
    type = models.IntegerField()
    experience = models.IntegerField(default=0)
    money = models.IntegerField(default=0)


class UserActivities(models.Model):
    auth_user = models.ForeignKey(User)
    activity = models.OneToOneField(Activity)
    is_answered = models.BooleanField(default=False)