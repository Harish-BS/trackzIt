from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from foundation.source.models import issue_source
from foundation.source.serializers import issue_sourceSerializer
from .serializers import issue_source_filterSerializer
response_message = 'Source'
error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def issue_source_list(request):
    if request.method == 'GET':
        tas = issue_source.objects.all()
        serializer = issue_sourceSerializer(tas, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = issue_sourceSerializer(data=request.data)
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
def issue_source_detail(request, pk):
    try:
        tas = issue_source.objects.get(pk=pk)
    except issue_source.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = issue_sourceSerializer(tas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = issue_sourceSerializer(tas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

@api_view(['POST'])
def issue_source_filter(request):
    try:
        if request.method == 'POST':
            serializer = issue_source_filterSerializer(data=request.data)
            if serializer.is_valid():
                client1 = serializer.validated_data.get('client')
                
                model_filter = issue_source.objects.all()
                
                if client1:
                    model_filter = model_filter.filter(client = client1)
                
                model_filter_data = issue_sourceSerializer(model_filter, many=True).data
                
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": model_filter_data
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except issue_source.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)