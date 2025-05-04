from django.contrib import admin
from django.urls import path, include
from learning_app import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_entry, name='create_entry'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('entry/<int:pk>/toggle/', views.toggle_entry_status, name='toggle_entry'),
    path('entry/<int:pk>/delete/', views.delete_entry, name='delete_entry'),
]