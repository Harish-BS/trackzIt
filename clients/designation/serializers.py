from rest_framework import serializers
from .models import Designation

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class designation_filterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Designation
        fields = ['client_id']