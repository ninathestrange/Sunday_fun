from django.http import HttpResponse


def index(request):
    return HttpResponse("Add leads here.")
