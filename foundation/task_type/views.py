from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from foundation.task_type.models import task_type
from foundation.task_type.serializers import task_typeSerializer
from .serializers import task_type_filterSerializer

response_message = 'Task_type'
error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def task_type_list(request):
    if request.method == 'GET':
        tas = task_type.objects.all()
        serializer = task_typeSerializer(tas, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = task_typeSerializer(data=request.data)
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
      #  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task_type_detail(request, pk):
    try:
        tas = task_type.objects.get(pk=pk)
    except task_type.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = task_typeSerializer(tas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = task_typeSerializer(tas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

@api_view(['POST'])
def task_type_filter(request):
    try:
        if request.method == 'POST':
            serializer = task_type_filterSerializer(data=request.data)
            if serializer.is_valid():
                client1 = serializer.validated_data.get('client')
                
                model_filter = task_type.objects.all()
                
                if client1:
                    model_filter = model_filter.filter(client = client1)
                
                model_filter_data = task_typeSerializer(model_filter, many=True).data
                
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": model_filter_data
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except task_type.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)