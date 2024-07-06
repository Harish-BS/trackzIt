from rest_framework import serializers
from core.feature.models import feature

class featureSerializer(serializers.ModelSerializer):
    class Meta:
        model = feature
        fields = '__all__'

class feature_filterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  feature
        fields = ['client','project_id','solution_id']