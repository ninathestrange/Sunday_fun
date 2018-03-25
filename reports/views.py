from django.http import HttpResponse


def index(request):
    return HttpResponse("Reports download here.")
