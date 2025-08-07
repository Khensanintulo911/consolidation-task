from django.db import models

class Post(models.Model):
    # Django will create an auto-incrementing primary key by default
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    default="Code by Khensani Ntulo"

    def __str__(self):
        return self.title

