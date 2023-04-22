from django.urls import path
from .import views

urlpatterns = [
   path('room/<int:pk>',views.room,name='room'),
   path('book/',views.booking,name='book'),

    

    ]