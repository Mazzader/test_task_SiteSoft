from django.db import models


class Hab(models.Model):
    title = models.CharField(max_length=300)
    link = models.CharField(max_length=1000, unique=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class Author(models.Model):
    nickname = models.CharField(max_length=300, unique=True)
    link = models.CharField(max_length=1000, unique=True)

    def __repr__(self):
        return self.nickname

    def __str__(self):
        return self.nickname


class Post(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    link = models.CharField(max_length=1000, unique=True)
    text = models.TextField(default='test')
    author = models.ForeignKey(to=Author, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
