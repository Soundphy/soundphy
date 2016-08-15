from rest_framework import serializers
from rest.models import Sound


class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ('sound', 'sha1', 'codec', 'size', 'duration',
                  'title', 'description', 'created', 'updated')
