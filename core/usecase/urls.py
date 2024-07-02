from django.urls import path, include
from core.usecase import views

urlpatterns = [
    path('core/',views.usecase_list),
    path('core/<int:pk>',views.usecase_detail),
]