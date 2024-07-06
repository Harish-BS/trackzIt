from django.urls import path, include
from foundation.priority import views

urlpatterns = [
    path('foundation/',views.priority_list),
    path('foundation/<int:pk>',views.priority_detail),
    path('foundation/filter',views.priority_filter),
]