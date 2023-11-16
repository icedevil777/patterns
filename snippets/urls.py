from django.contrib import admin
from django.urls import path, include
from my_auth.views import UserViewSet
from rest_framework import routers
from snippets import views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
