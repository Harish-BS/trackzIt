from django.urls import path, include
from foundation.complexity import views

urlpatterns = [
    path('foundation/',views.complexity_list),
    path('foundation/<int:pk>',views.complexity_detail),
    path('foundation/filter',views.complexity_filter),
]