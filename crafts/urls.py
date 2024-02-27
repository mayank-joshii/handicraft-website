from django.contrib import admin
from django.urls import path, include
from crafts import views
urlpatterns = [
    path('',views.index, name='home'),
    path('gallary',views.gallary, name='gallary'),
    path('contact',views.contact, name='contact'),
    path('about',views.about, name='about')
]
