from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Ressource(models.Model):
    VIDEO = 'V'
    IMAGE = 'I'
    PDF = 'P'
    TYPE_CHOICES = [
        (VIDEO, 'Vidéo'),
        (IMAGE, 'Image'),
        (PDF, 'Document PDF')
    ]
    title = models.CharField(max_length=200)
    ressource_type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=IMAGE
    )
    file = models.FileField(upload_to='ressources/')
    def __str__(self):
        return self.title

class Commentaire(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Article(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to="articles")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ressources = models.ManyToManyField(Ressource, blank=True)
    commentaires = models.ManyToManyField(Commentaire, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Cours(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article, blank=True)
    commentaires = models.ManyToManyField(Commentaire, blank=True)

    def __str__(self):
        return self.title