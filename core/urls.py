from django.urls import path
from app.views import index, get_data

urlpatterns = [
    path('', index),
    path('get_data/', get_data)
]
