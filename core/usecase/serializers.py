from rest_framework import serializers
from core.usecase.models import usecase

class usecaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = usecase
        fields = '__all__'


class usecase_filterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  usecase
        fields = ['client','project_id','solution_id','feature_id']