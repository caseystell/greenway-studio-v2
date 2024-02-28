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
  path('projects/kinective', views.kinective, name='kinective'),
  path('projects/atlantic-aviation', views.atlantic_aviation, name='atlantic-aviation'),
  path('projects/camelot-clinic', views.camelot_clinic, name='camelot-clinic'),
  path('projects/playa-drain', views.playa_drain, name='playa-drain'),
  path('projects/university-ave', views.univ_ave, name='univ-ave'),
  path('projects/westfall-apts', views.westfall_apts, name='westfall-apts'),
  path('projects/spray-parks', views.spray_parks, name='spray-parks'),
]