from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DesignationViewSet
from clients.designation import views
router = DefaultRouter()
router.register(r'designations', DesignationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('clients/',views.designation_list),
    path('clients/<int:pk>',views.designation_detail),
]