

from django.urls import path
from django.http import HttpResponse,HttpRequest,JsonResponse
def index(request:HttpRequest):
    a = request.GET['a']
    b = request.GET['b']
    return JsonResponse({
        'result':a+b
    })

urlpatterns = [
    path('', index),
]
