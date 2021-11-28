from django.db import models
from slugify import slugify
from django.conf import settings


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    viewed = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200, unique=True)
    vote = models.IntegerField(default=0)
    bookmark_count = models.IntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    detail = models.TextField()
    answers = models.ManyToManyField('Answer')
    tags = models.ManyToManyField('Tag')

    def on_create(self):
        self.slug = slugify(self.title)
        self.save()


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    viewed = models.IntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    detail = models.TextField()
    vote = models.IntegerField(default=0)
    marked_as_answer = models.BooleanField(default=False)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def on_create(self):
        self.slug = slugify(self.name)
        self.save()
