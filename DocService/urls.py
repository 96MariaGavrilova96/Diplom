from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registrationBook/', views.registrationBook, name='registrationBook'),
    path('addDocument/', views.addDocument, name='addDocument'),
    path('readDocument/<number>/', views.readDocument, name='readDocument'),
    path('editDocumment/<number>/', views.editDocument, name='editDocument'),
    path('removeDocumment/<number>/', views.removeDocumment, name='removeDocumment'),
    path('csvView/', views.csvView, name='csvView'),
]