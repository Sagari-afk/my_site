"""from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
"""

from rest_framework import routers

from .views import UserViewSet


router = routers.DefaultRouter()
router.register('api/v1/user', UserViewSet, 'user')

urlpatterns = router.urls
