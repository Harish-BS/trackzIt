from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet
from clients.department import views

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('clients/',views.department_list),
    path('clients/<int:pk>',views.department_detail),
]