from rest_framework import serializers
from core.task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class Task_filterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Task
        fields = ['client_id','project_id','solution_id','feature_id','usecase_id','priority_id','user_id','department_id','issue_stage_id','issue_source_id','issue_type_id','complexity_id','sdlc_id','status_id']