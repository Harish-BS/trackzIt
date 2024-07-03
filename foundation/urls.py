from django.urls import path, include

urlpatterns = [
    path('priority/', include('foundation.priority.urls')),
    path('status/', include('foundation.status.urls')),
    path('task_type/', include('foundation.task_type.urls')),
    path('SDLC/', include('foundation.sdlc.urls')),
    path('complexity/', include('foundation.complexity.urls')),
    path('issue_type/', include('foundation.issue_type.urls')),
    path('issue_source/', include('foundation.source.urls')),
    path('issue_stage/', include('foundation.stage.urls')),
]