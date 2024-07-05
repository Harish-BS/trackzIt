from core.task.models import Task
from .serializers import TaskSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
response_message = 'Task'
error_message = 'Something went wrong. Please try again later.'
#error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        use = Task.objects.all()
        serializer = TaskSerializer(use, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
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
        #return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        client = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

