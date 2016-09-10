from rest_framework import serializers
from rest.models import SoundFile
from rest.models import SoundInformation


SOUND_INFO = ('title', 'description')
SOUND_FILE = ('sha1', 'codec', 'size', 'duration')
SOUND_EXTRA = ('created', 'updated')


class SoundFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundFile
        fields = ('sound', 'sha1', 'codec', 'size', 'duration', 'uploaded')
        extra_kwargs = {
            'sound': {'write_only': True}
        }


class SoundInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundInformation
        fields = ('sound', 'title', 'description')
        extra_kwargs = {
            'sound': {'read_only': True}
        }


class SoundFileInformationSerializer(serializers.ModelSerializer):
    sound = SoundFileSerializer()

    class Meta:
        model = SoundInformation
        fields = ('sound', 'title', 'description', 'added')

    def create(self, validated_data):
        soundfile = SoundFile.objects.create(
            sound=validated_data['sound']['sound'],
            sha1=validated_data['sha1'],
            codec=validated_data['codec'],
            size=validated_data['size'],
            duration=validated_data['duration'],
        )
        soundfile.save()
        soundinfo = SoundInformation.objects.create(
            sound=soundfile,
            title=validated_data['title'],
            description=validated_data['description'],
        )
        return soundinfo
