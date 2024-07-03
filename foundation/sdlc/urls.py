from django.urls import path, include
from foundation.sdlc import views

urlpatterns = [
    path('foundation/',views.SDLC_list),
    path('foundation/<int:pk>',views.SDLC_detail),
]