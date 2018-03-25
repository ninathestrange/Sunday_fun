from django.http import HttpResponse


def index(request):
    return HttpResponse("Next page after login. You chose what to do next here")
