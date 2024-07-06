from rest_framework import serializers
from core.solution.models import solution

class solutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = solution
        fields = '__all__'

class solution_filterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  solution
        fields = ['client','project_id']