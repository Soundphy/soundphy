from django.db import models


class Sound(models.Model):
    sound = models.FileField(upload_to='upload/sounds')
    # Missing <language> model
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Missing <keywords> model
    # Missing <category> model

    sha1 = models.CharField(max_length=40)  # TODO: length must be 40 always
    codec = models.CharField(max_length=30)
    size = models.IntegerField()
    duration = models.FloatField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
