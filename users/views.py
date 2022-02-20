"""from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the users index.")

"""
from rest_framework import viewsets, permissions

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
