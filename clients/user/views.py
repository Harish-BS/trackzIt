from rest_framework import viewsets
from clients.user.models import User
from .serializers import UserSerializer
from .serializers import user_filterSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
response_message = 'User'
error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        use = User.objects.all()
        serializer = UserSerializer(use, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" added successfully",
                "data": serializer.data
            }
            return Response(response)
        error = {
                "status": False,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "status_message": error_message,
                "error": serializer.errors
            }
        return Response(error)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        client = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

@api_view(['POST'])
def user_filter(request):
    try:
        if request.method == 'POST':
            serializer = user_filterSerializer(data=request.data)
            if serializer.is_valid():
                client = serializer.validated_data.get('client_id')
                desg = serializer.validated_data.get('designation_id')
                dept = serializer.validated_data.get('department_id')
                
                model_filter = User.objects.all()
                
                if client:
                    model_filter = model_filter.filter(client_id = client)
                if desg:
                    model_filter = model_filter.filter(designation_id = desg)
                if dept:
                    model_filter = model_filter.filter(department_id = dept)
                
                model_filter_data = UserSerializer(model_filter, many=True).data
                print(model_filter)
                
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": model_filter_data
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)