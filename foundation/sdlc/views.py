from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from foundation.sdlc.models import SDLC
from foundation.sdlc.serializers import SDLCSerializer

@api_view(['GET', 'POST'])
def SDLC_list(request):
    if request.method == 'GET':
        tas = SDLC.objects.all()
        serializer = SDLCSerializer(tas, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": "Message",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = SDLCSerializer(data=request.data)
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
def SDLC_detail(request, pk):
    try:
        tas = SDLC.objects.get(pk=pk)
    except SDLC.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SDLCSerializer(tas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SDLCSerializer(tas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

