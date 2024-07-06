from django.urls import path, include
from core.solution import views

urlpatterns = [
    path('core/',views.solution_list),
    path('core/<int:pk>',views.solution_detail),
    path('core/filter',views.solution_filter),
]