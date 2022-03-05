from django.http import HttpResponse


def helloworldfunction(request):
    returnobject = HttpResponse('<h1>hello world</h1>')
    return returnobject