from django.db import models


class Sound(models.Model):
    sound = models.FileField(upload_to='upload/sounds')
    # Missing <language> model
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Missing <keywords> model
    # Missing <category> model

    # TODO: length must be 40 always
    sha1 = models.CharField(editable=False, max_length=40, unique=True)
    codec = models.CharField(editable=False, max_length=30)
    size = models.IntegerField(editable=False)
    duration = models.FloatField(editable=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
