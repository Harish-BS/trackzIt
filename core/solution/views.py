from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.solution.models import solution
from core.solution.serializers import solutionSerializer
from .serializers import solution_filterSerializer
response_message = 'Solution'
error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def solution_list(request):
    if request.method == 'GET':
        sol = solution.objects.all()
        serializer = solutionSerializer(sol, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = solutionSerializer(data=request.data)
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
def solution_detail(request, pk):
    try:
        sol = solution.objects.get(pk=pk)
    except solution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = solutionSerializer(sol)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = solutionSerializer(sol, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sol.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

@api_view(['POST'])
def solution_filter(request):
    try:
        if request.method == 'POST':
            serializer = solution_filterSerializer(data=request.data)
            if serializer.is_valid():
                client1 = serializer.validated_data.get('client')
                proj = serializer.validated_data.get('project_id')
                
                model_filter = solution.objects.all()
                
                if client1:
                    model_filter = model_filter.filter(client = client1)

                if proj:
                    model_filter = model_filter.filter(project_id = proj)
                
                model_filter_data = solutionSerializer(model_filter, many=True).data
                
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": model_filter_data
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except solution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)