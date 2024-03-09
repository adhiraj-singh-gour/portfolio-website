from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('education/',education,name='education'),
    path('project/',projects,name='projects'),
    path('contact/',contact,name='contact'),


]