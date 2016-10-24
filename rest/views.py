import hashlib

from rest.models import Sound
from rest.serializers import SoundListCreateSerializer
from rest.serializers import SoundRetrieveUpdateDestroySerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


def hashfile(afile, hasher, blocksize=65536):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.digest()


class SoundList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Sound.objects.all()
    serializer_class = SoundListCreateSerializer

    def perform_create(self, serializer):
        sound = self.request._files['sound']
        codec = sound.content_type.split('/')[-1]
        size = sound._size
        duration = 0.0  # TODO
        tempfile = self.request._files['sound'].file.name
        sha1 = hashfile(open(tempfile, 'rb'), hashlib.sha1()).hex()
        self.request._files['sound']._name = sha1
        # TODO: validate calculated parameters before saving
        # TODO: if file already uploaded, do not save
        serializer.save(codec=codec, size=size, duration=duration, sha1=sha1)


class SoundDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Sound.objects.all()
    serializer_class = SoundRetrieveUpdateDestroySerializer
