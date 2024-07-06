from rest_framework import serializers
from core.task_history.models import task_history

class Task_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = task_history
        fields = '__all__'

class Task_history_filterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  task_history
        fields = ['client_id','project_id','solution_id','feature_id','usecase_id','priority_id','user_id','department_id','issue_stage_id','issue_source_id','issue_type_id','complexity_id','sdlc_id','status_id']