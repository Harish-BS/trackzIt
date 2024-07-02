from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.usecase.models import usecase
from core.usecase.serializers import usecaseSerializer

@api_view(['GET', 'POST'])
def usecase_list(request):
    if request.method == 'GET':
        sol = usecase.objects.all()
        serializer = usecaseSerializer(sol, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": "Message",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = usecaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": "Message",
                "data": serializer.data
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def usecase_detail(request, pk):
    try:
        sol = usecase.objects.get(pk=pk)
    except usecase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = usecaseSerializer(sol)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = usecaseSerializer(sol, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sol.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################


