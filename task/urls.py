from django.conf.urls import url
from task import views

urlpatterns = [
    url(r'add/', views.add, name='add'),
    url(r'check/', views.check, name='add'),
    url(r'result/', views.result, name='add'),
]