from rest_framework import serializers
from foundation.complexity.models import complexity

class complexitySerializer(serializers.ModelSerializer):
    class Meta:
        model = complexity
        fields = '__all__'