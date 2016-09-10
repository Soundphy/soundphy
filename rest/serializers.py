from rest_framework import serializers
from rest.models import Sound


SOUND_INFO = ('title', 'description')
SOUND_FILE = ('sha1', 'codec', 'size', 'duration')
SOUND_EXTRA = ('created', 'updated')


class SoundListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ('sound', ) + SOUND_INFO + SOUND_FILE
        extra_kwargs = {
            'sound': {'write_only': True}
        }


class SoundRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = SOUND_INFO + SOUND_FILE + SOUND_EXTRA
