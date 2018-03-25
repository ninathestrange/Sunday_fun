from django.http import HttpResponse


def index(request):
    return HttpResponse("All data will be here")
