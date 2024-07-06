from django.urls import path, include
from foundation.stage import views

urlpatterns = [
    path('foundation/',views.issue_stage_list),
    path('foundation/<int:pk>',views.issue_stage_detail),
    path('foundation/filter',views.issue_stage_filter),
]