from django.urls import path

from .views import index
from .views import contato
from .views import produto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
]