from rest_framework import serializers
from foundation.issue_type.models import issue_type

class issue_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = issue_type
        fields = '__all__'