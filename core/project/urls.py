from django.urls import path, include
from core.project import views

urlpatterns = [
    path('core/',views.project_list),
    path('core/<int:pk>',views.project_detail),
]