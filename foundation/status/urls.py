from django.urls import path, include
from foundation.status import views

urlpatterns = [
    path('foundation/',views.status_list),
    path('foundation/<int:pk>',views.status_detail),
    path('foundation/filter',views.status_filter),
]