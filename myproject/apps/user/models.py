from django.db import models

SUCCESS = 1
ERR_BAD_CREDENTIALS = -1 
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LENGTH = 128
MAX_PASSWORD_LENGTH = 128

class UserManager(models.Manager):
    def login(self, user, password):
        try:
            user = User.objects.get(user = user, password = password)
            user.count += 1
            user.save()
            return user.count
        except User.DoesNotExist:
            return ERR_BAD_CREDENTIALS

    def add(self, user, password=""):
        if user == "" or len(user) > MAX_USERNAME_LENGTH:
            return ERR_BAD_USERNAME
        elif len(password) > MAX_PASSWORD_LENGTH:
            return ERR_BAD_PASSWORD
        else:
            try:
                user = User.objects.get(user=user)
                return ERR_USER_EXISTS
            except User.DoesNotExist:
                user = User(user=user, password = password, count=1)
                user.save()
                return user.count

    def TESTAPI_resetFixture(self):
        User.objects.all().delete()
        return SUCCESS

class User(models.Model):
    objects = UserManager()
    user = models.CharField(max_length=MAX_USERNAME_LENGTH, unique=True)
    password = models.CharField(max_length=MAX_PASSWORD_LENGTH, default="")
    count = models.IntegerField(default=0)