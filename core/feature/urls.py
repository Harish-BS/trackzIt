from django.urls import path, include
from core.feature import views

urlpatterns = [
    path('core/',views.feature_list),
    path('core/<int:pk>',views.feature_detail),
]