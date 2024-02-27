from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('contact/', views.contact, name='contact'),
  path('portfolio/', views.portfolio, name='portfolio'),
  path('about/mission', views.mission, name='mission'),
  path('about/our-story', views.our_story, name='our-story'),
  path('projects/alameda', views.alameda, name='alameda'),
  path('projects/sisd-carrasco', views.sisd_carrasco, name='sisd-carrasco'),
  path('projects/ttuhsc', views.ttuhsc, name='ttuhsc'),
  path('projects/eastside-reg', views.eastside_reg, name='eastside-reg'),
  path('projects/franklin-mts-aviation', views.franklin_mts_aviation, name='franklin-mts-aviation'),
  path('projects/borderland-park', views.borderland_park, name='borderland-park'),
  path('projects/thorn-park', views.thorn_park, name='thorn-park'),
  path('projects/north-loop-apts', views.north_loop_apts, name='north-loop-apts'),
]