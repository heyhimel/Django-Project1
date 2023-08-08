from email.mime import image
from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    #summery=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name # aita amra create kore rakhlam,aitar use holo aita admin er table er moddhe ai models er name dekhabe.


class signup(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    username=models.CharField(max_length=20)
    


class upload_picture(models.Model):
    image = models.ImageField(upload_to='images/', default=None)
    