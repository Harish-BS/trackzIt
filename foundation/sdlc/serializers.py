from rest_framework import serializers
from foundation.sdlc.models import SDLC

class SDLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = SDLC
        fields = '__all__'


class SDLC_filterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  SDLC
        fields = ['client']