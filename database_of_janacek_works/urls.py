from django.conf.urls import url, patterns
from . import views
from database_of_janacek_works.views import PieceListRenderer

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^piece/$',PieceListRenderer.as_view(), name='piece_list'),
 #   url(r'^album/$',AlbumListRenderer.as_view()),
    #url(r'^rest/piece/$',views.PieceListJson.as_view(), name='rest_piece_data'),

)