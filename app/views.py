from django.http import HttpResponse,HttpRequest,JsonResponse
import json
def index(request:HttpRequest):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    return JsonResponse({
        'result':int(a)+int(b)
    })

def get_data(request: HttpRequest):
    if request.method == 'GET':
        print('GET')

    if request.method == 'POST':
        data = request.body.decode()
        data_a = json.loads(data)
        a = data_a['a']
        b = data_a['b']

    return JsonResponse({
        'result': int(a) + int(b)
    })