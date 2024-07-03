from rest_framework import serializers
from foundation.source.models import issue_source

class issue_sourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = issue_source
        fields = '__all__'