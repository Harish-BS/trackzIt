from rest_framework import serializers
from core.task_history.models import task_history

class Task_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = task_history
        fields = '__all__'