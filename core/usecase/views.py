from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.usecase.models import usecase
from core.usecase.serializers import usecaseSerializer
from .serializers import usecase_filterSerializer
response_message = 'Usecase'
error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def usecase_list(request):
    if request.method == 'GET':
        sol = usecase.objects.all()
        serializer = usecaseSerializer(sol, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
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

@api_view(['POST'])
def usecase_filter(request):
    try:
        if request.method == 'POST':
            serializer = usecase_filterSerializer(data=request.data)
            if serializer.is_valid():
                client1 = serializer.validated_data.get('client')
                proj = serializer.validated_data.get('project_id')
                sol = serializer.validated_data.get('solution_id')
                feat = serializer.validated_data.get('feature_id')

                model_filter = usecase.objects.all()
                
                if client1:
                    model_filter = model_filter.filter(client = client1)

                if proj:
                    model_filter = model_filter.filter(project_id = proj)

                if sol:
                    model_filter = model_filter.filter(solution_id = sol)

                if feat:
                    model_filter = model_filter.filter(feature_id = feat)
                
                model_filter_data = usecaseSerializer(model_filter, many=True).data
                
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": model_filter_data
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except usecase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)