from django.urls import path
from .views import *
urlpatterns = [
path('',listuser),
path('Update/<id>/',Update,name='updateuser'),
path('Delete/<id>/',Delete,name='deleteuser'),
]
