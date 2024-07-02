from rest_framework import serializers
from core.usecase.models import usecase

class usecaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = usecase
        fields = '__all__'