from django.urls import path
from .  import views

urlpatterns = [
    path('', views.home , name='home'),
    path('listings/', views.listings , name='listings'),
    path('details/<int:room_id>/', views.details , name="details"),
    path('login/', views.login , name='login'),
    path('logout/', views.logout , name='logout'),
    path('register/', views.register, name='register'),

]
