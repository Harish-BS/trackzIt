from django.urls import path, include
from core.task import views

urlpatterns = [
    path('core/',views.task_list),
    path('core/<int:pk>',views.task_detail),
]