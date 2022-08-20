from django.http import JsonResponse

def controles(request):
    if request.method == 'GET':
        controle = {'id': 1, 'nome':'teste'}
        return JsonResponse(controle)
