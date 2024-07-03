from rest_framework import serializers
from foundation.stage.models import issue_stage

class issue_stageSerializer(serializers.ModelSerializer):
    class Meta:
        model = issue_stage
        fields = '__all__'