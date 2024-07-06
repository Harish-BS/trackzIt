from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from foundation.stage.models import issue_stage
from foundation.stage.serializers import issue_stageSerializer
from .serializers import issue_stage_filterSerializer
response_message = 'Stage'
error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def issue_stage_list(request):
    if request.method == 'GET':
        tas = issue_stage.objects.all()
        serializer = issue_stageSerializer(tas, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = issue_stageSerializer(data=request.data)
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
def issue_stage_detail(request, pk):
    try:
        tas = issue_stage.objects.get(pk=pk)
    except issue_stage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = issue_stageSerializer(tas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = issue_stageSerializer(tas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

@api_view(['POST'])
def issue_stage_filter(request):
    try:
        if request.method == 'POST':
            serializer = issue_stage_filterSerializer(data=request.data)
            if serializer.is_valid():
                client1 = serializer.validated_data.get('client')
                
                model_filter = issue_stage.objects.all()
                
                if client1:
                    model_filter = model_filter.filter(client = client1)
                
                model_filter_data = issue_stageSerializer(model_filter, many=True).data
                
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": model_filter_data
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except issue_stage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)