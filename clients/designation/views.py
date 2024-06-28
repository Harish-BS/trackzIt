from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Designation
from .serializers import DesignationSerializer
from rest_framework.decorators import api_view 

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


@api_view(['GET', 'POST'])
def designation_list(request):
    if request.method == 'GET':
        desg = Designation.objects.all()
        serializer = DesignationSerializer(desg, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": "Message",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = DesignationSerializer(data=request.data)
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
        
@api_view(['GET','PUT','DELETE'])

def designation_detail(request,pk):
    try:
        desg = Designation.objects.get(pk=pk)
    except Designation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = DesignationSerializer(desg)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = DesignationSerializer(desg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        desg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)