from rest_framework import serializers
from foundation.task_type.models import task_type

class task_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = task_type
        fields = '__all__'

class task_type_filterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  task_type
        fields = ['client']