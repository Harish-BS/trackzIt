from rest_framework import viewsets
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


@api_view(['GET', 'POST'])
def department_list(request):
    if request.method == 'GET':
        depat = Department.objects.all()
        serializer = DepartmentSerializer(depat, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": "Message",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = DepartmentSerializer(data = request.data)
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
def department_detail(request, pk):
    try:
        depat = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializer(depat)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DepartmentSerializer(depat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        depat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    