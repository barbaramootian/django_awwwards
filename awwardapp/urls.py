from django.urls import path  
from django.contrib import admin  
from . import views  
  
urlpatterns = [  
   path('',views.index, name='index'),
   path('accounts/profile/', views.index, name="index"),
   path('signout/', views.logoutUser, name='signout'),
]
  