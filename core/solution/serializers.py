from rest_framework import serializers
from core.solution.models import solution

class solutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = solution
        fields = '__all__'