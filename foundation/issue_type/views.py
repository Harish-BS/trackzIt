from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from foundation.issue_type.models import issue_type
from foundation.issue_type.serializers import issue_typeSerializer
response_message = 'Issue_type'
error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def issue_type_list(request):
    if request.method == 'GET':
        tas = issue_type.objects.all()
        serializer = issue_typeSerializer(tas, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = issue_typeSerializer(data=request.data)
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
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def issue_type_detail(request, pk):
    try:
        tas = issue_type.objects.get(pk=pk)
    except issue_type.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = issue_typeSerializer(tas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = issue_typeSerializer(tas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

