from rest_framework import serializers
from foundation.status.models import statuss

class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = statuss
        fields = '__all__'