from django.urls import path
from .  import views
from .views import *

urlpatterns = [
    path('', views.home , name='home'),
    path('listings/', views.listings , name='listings'),
    path('details/<int:room_id>/', views.details , name="details"),
    path('room/<int:room_id>/',RoomDetailView.as_view(),name = 'room_detail'),
    path('login/', views.login , name='login'),
    path('logout/', views.logout , name='logout'),
    path('register/', views.register, name='register'),

]
