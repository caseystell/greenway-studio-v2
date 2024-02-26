from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('contact/', views.contact, name='contact'),
  path('portfolio/', views.portfolio, name='portfolio'),
  path('about/clients', views.clients, name='clients'),
  path('about/mission', views.mission, name='mission'),
  path('about/our-story', views.our_story, name='our-story'),
]