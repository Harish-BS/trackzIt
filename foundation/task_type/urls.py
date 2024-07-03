from django.urls import path, include
from foundation.task_type import views

urlpatterns = [
    path('foundation/',views.task_type_list),
    path('foundation/<int:pk>',views.task_type_detail),
]