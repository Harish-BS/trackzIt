from django.urls import path, include
from foundation.source import views

urlpatterns = [
    path('foundation/',views.issue_source_list),
    path('foundation/<int:pk>',views.issue_source_detail),
]