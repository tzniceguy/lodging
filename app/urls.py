from django.urls import path
from .views import ListLodge, ListUsers

urlpatterns = [
    path('users/', ListUsers.as_view()),
    path('lodges/', ListLodge.as_view())
]
