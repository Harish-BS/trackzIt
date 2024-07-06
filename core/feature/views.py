from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.feature.models import feature
from core.feature.serializers import featureSerializer
from .serializers import feature_filterSerializer
response_message = 'Feature'
error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def feature_list(request):
    if request.method == 'GET':
        tas = feature.objects.all()
        serializer = featureSerializer(tas, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = featureSerializer(data=request.data)
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
def feature_detail(request, pk):
    try:
        tas = feature.objects.get(pk=pk)
    except feature.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = featureSerializer(tas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = featureSerializer(tas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

@api_view(['POST'])
def feature_filter(request):
    try:
        if request.method == 'POST':
            serializer = feature_filterSerializer(data=request.data)
            if serializer.is_valid():
                client1 = serializer.validated_data.get('client')
                proj = serializer.validated_data.get('project_id')
                sol = serializer.validated_data.get('solution_id')
                
                model_filter = feature.objects.all()
                
                if client1:
                    model_filter = model_filter.filter(client = client1)

                if proj:
                    model_filter = model_filter.filter(project_id = proj)
                if sol:
                    model_filter = model_filter.filter(solution_id = sol)
                
                model_filter_data = featureSerializer(model_filter, many=True).data
                
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": model_filter_data
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except feature.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)