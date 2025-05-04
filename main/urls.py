# main/urls.py
from django.urls import include, path
from .views import navigation_view, register


app_name = 'learning_site'

urlpatterns = [
    path('', navigation_view, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]