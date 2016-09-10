import hashlib

from rest.models import SoundFile
from rest.models import SoundInformation
from rest.serializers import SoundFileSerializer
from rest.serializers import SoundInformationSerializer
from rest.serializers import SoundFileInformationSerializer
from rest_framework import generics


def hashfile(afile, hasher, blocksize=65536):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.digest()


class SoundList(generics.ListCreateAPIView):
    queryset = SoundInformation.objects.all()
    serializer_class = SoundFileInformationSerializer

    def perform_create(self, serializer):
        sound = self.request._files['sound.sound']
        codec = sound.content_type.split('/')[-1]
        size = sound._size
        duration = 0.0  # TODO
        tempfile = sound.file.name
        sha1 = hashfile(open(tempfile, 'rb'), hashlib.sha1()).hex()
        sound._name = sha1
        # TODO: validate calculated parameters before saving
        # TODO: if file already uploaded, do not save
        serializer.save(codec=codec, size=size, duration=duration, sha1=sha1)


class SoundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoundInformation.objects.all()
    serializer_class = SoundInformationSerializer
