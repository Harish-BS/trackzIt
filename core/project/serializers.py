from rest_framework import serializers
from core.project.models import project

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'

class project_filterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  project
        fields = ['client']