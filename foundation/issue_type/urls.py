from django.urls import path, include
from foundation.issue_type import views

urlpatterns = [
    path('foundation/',views.issue_type_list),
    path('foundation/<int:pk>',views.issue_type_detail),
]