from django.http import HttpResponse
from .permissions import create_custom_permissions


def initialize_permissions(request):
    create_custom_permissions()
    return HttpResponse('Done')
