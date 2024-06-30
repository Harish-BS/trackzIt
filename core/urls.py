from django.urls import path, include

urlpatterns = [
    path('project/', include('core.project.urls')),
    #path('solution/', include('core.solution.urls')),
    #path('feature/', include('core.feature.urls')),
    #path('usecase/', include('core.usecase.urls')),
    #path('task/', include('core.task.urls')),
    #path('task_history/', include('core.task_history.urls')),
]