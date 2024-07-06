from rest_framework import serializers
from clients.user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class user_filterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ['client_id','designation_id','department_id']