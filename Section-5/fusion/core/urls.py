from django.urls import path
from .views import IndexView, Teste404View, Teste500View

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('teste404/', Teste404View.as_view(), name='teste404'),
    path('teste500/', Teste500View.as_view(), name='teste500'),
]