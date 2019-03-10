from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()


class userdb(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    salary = models.CharField(max_length=10)
