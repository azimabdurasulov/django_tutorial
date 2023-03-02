from django.http import HttpResponse,HttpRequest,JsonResponse
def index(request:HttpRequest):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    return JsonResponse({
        'result':int(a)+int(b)
    })