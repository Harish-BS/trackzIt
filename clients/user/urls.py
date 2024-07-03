from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from clients.user import views
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('clients/',views.user_list),
    path('clients/<int:pk>',views.user_detail),
]