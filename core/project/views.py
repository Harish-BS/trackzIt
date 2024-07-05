from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.project.models import project
from core.project.serializers import projectSerializer
response_message = 'Project'
error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def project_list(request):
    if request.method == 'GET':
        proj = project.objects.all()
        serializer = projectSerializer(proj, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = projectSerializer(data=request.data)
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
def project_detail(request, pk):
    try:
        proj = project.objects.get(pk=pk)
    except project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = projectSerializer(proj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = projectSerializer(proj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        proj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

