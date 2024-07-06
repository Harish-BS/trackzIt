from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from foundation.status.models import statuss
from foundation.status.serializers import statusSerializer
from .serializers import status_filterSerializer
response_message = 'Status'
error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def status_list(request):
    if request.method == 'GET':
        tas = statuss.objects.all()
        serializer = statusSerializer(tas, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = statusSerializer(data=request.data)
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
       # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def status_detail(request, pk):
    try:
        tas = statuss.objects.get(pk=pk)
    except statuss.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = statusSerializer(tas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = statusSerializer(tas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

@api_view(['POST'])
def status_filter(request):
    try:
        if request.method == 'POST':
            serializer = status_filterSerializer(data=request.data)
            if serializer.is_valid():
                client1 = serializer.validated_data.get('client')
                
                model_filter = statuss.objects.all()
                
                if client1:
                    model_filter = model_filter.filter(client = client1)
                
                model_filter_data = statusSerializer(model_filter, many=True).data
                
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": model_filter_data
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except statuss.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)