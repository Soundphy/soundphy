from rest_framework import serializers
from rest.models import Sound


class SoundSerializer(serializers.ModelSerializer):
    sha1 = serializers.ReadOnlyField()
    codec = serializers.ReadOnlyField()
    size = serializers.ReadOnlyField()
    duration = serializers.ReadOnlyField()
    class Meta:
        model = Sound
        fields = ('sound', 'sha1', 'codec', 'size', 'duration',
                  'title', 'description', 'created', 'updated')
