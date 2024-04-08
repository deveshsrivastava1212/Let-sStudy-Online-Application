from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='Login'),
    path('logout/', views.logoutUser, name='Logout'),
    path('register/', views.registerPage, name='Register'),
    path('', views.home, name='Home'),
    path('room/<str:pk>/', views.room, name='Room'),
    path('profile/<str:pk>/', views.userProfile, name='Profile'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name="Update-Room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    
]