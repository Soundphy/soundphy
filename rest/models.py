from django.db import models


class SoundFile(models.Model):
    sound = models.FileField(upload_to='upload/sounds')

    sha1 = models.CharField(editable=False, max_length=40, unique=True)  # TODO: length must be 40 always
    codec = models.CharField(editable=False, max_length=30)
    size = models.IntegerField(editable=False)
    duration = models.FloatField(editable=False)

    uploaded = models.DateTimeField(auto_now_add=True)


class SoundInformation(models.Model):
    sound = models.ForeignKey(SoundFile, on_delete=models.CASCADE)

    # Missing <language> model
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Missing <keywords> model
    # Missing <category> model

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
