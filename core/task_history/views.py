from core.task_history.models import task_history
from .serializers import Task_historySerializer
from .serializers import Task_history_filterSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
response_message = 'Task_history'
error_message = 'Something went wrong. Please try again later.'
@api_view(['GET', 'POST'])
def task_history_list(request):
    if request.method == 'GET':
        use = task_history.objects.all()
        serializer = Task_historySerializer(use, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": response_message+" provided successfully",
                "data": serializer.data
        }
        return Response(response)
    elif request.method == 'POST':
        serializer = Task_historySerializer(data=request.data)
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
def task_history_detail(request, pk):
    try:
        client = task_history.objects.get(pk=pk)
    except task_history.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Task_historySerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Task_historySerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################################################################################################################

@api_view(['POST'])
def task_history_filter(request):
    try:
        if request.method == 'POST':
            serializer = Task_history_filterSerializer(data=request.data)
            if serializer.is_valid():
                client1 = serializer.validated_data.get('client_id')
                proj = serializer.validated_data.get('project_id')
                sol = serializer.validated_data.get('solution_id')
                feat = serializer.validated_data.get('feature_id')
                usec = serializer.validated_data.get('usecase_id')
                prio = serializer.validated_data.get('priority_id')
                use = serializer.validated_data.get('user_id')
                dept = serializer.validated_data.get('department_id')
                stag = serializer.validated_data.get('issue_stage_id')
                sour = serializer.validated_data.get('issue_source_id')
                typ = serializer.validated_data.get('issue_type_id')
                compl = serializer.validated_data.get('complexity_id')
                sdl = serializer.validated_data.get('sdlc_id')
                stat = serializer.validated_data.get('status_id')

                model_filter = task_history.objects.all()
                
                if client1:
                    model_filter = model_filter.filter(client_id = client1)

                if proj:
                    model_filter = model_filter.filter(project_id = proj)

                if sol:
                    model_filter = model_filter.filter(solution_id = sol)

                if feat:
                    model_filter = model_filter.filter(feature_id = feat)

                if usec:
                    model_filter = model_filter.filter(usecase_id = usec)

                if prio:
                    model_filter = model_filter.filter(priority_id = prio)

                if use:
                    model_filter = model_filter.filter(user_id = use)
                
                if dept:
                    model_filter = model_filter.filter(department_id = dept)

                if stag:
                    model_filter = model_filter.filter(issue_stage_id = stag)

                if sour:
                    model_filter = model_filter.filter(issue_source_id = sour)

                if typ:
                    model_filter = model_filter.filter(issue_type_id = typ)

                if compl:
                    model_filter = model_filter.filter(complexity_id = compl)

                if sdl:
                    model_filter = model_filter.filter(sdlc_id = sdl)

                if stat:
                    model_filter = model_filter.filter(status_id = stat)
                
                model_filter_data = Task_historySerializer(model_filter, many=True).data
                
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": model_filter_data
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except task_history.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)