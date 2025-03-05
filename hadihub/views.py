from django.http import HttpResponse

def aboutme(request):
    return HttpResponse('All about me!')