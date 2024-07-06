from django.urls import path, include
from core.task_history import views

urlpatterns = [
    path('core/',views.task_history_list),
    path('core/<int:pk>',views.task_history_detail),
    path('core/filter',views.task_history_filter),
]