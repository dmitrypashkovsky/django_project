from django.conf.urls import url
from task import views

urlpatterns = [
    url(r'add/', views.add, name='add'),
    url(r'check/', views.add, name='check'),
    url(r'result/', views.add, name='result'),
]