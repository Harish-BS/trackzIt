from rest_framework import serializers
from foundation.priority.models import priority

class prioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = priority
        fields = '__all__'