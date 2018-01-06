from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=16)
    user_sign = models.BooleanField(default=False)


class Hospital(models.Model):
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=500)
    

class Feedback(models.Model):
    user_id = models.ForeignKey(User) 
    user_email = models.EmailField()
    content = models.TextField()
