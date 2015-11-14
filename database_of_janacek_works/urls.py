from django.conf.urls import url, patterns
from . import views
from database_of_janacek_works.views import PieceListJson, AlbumListJson


urlpatterns = patterns('',
    url(r'^piece/$', views.piece, name='piece'),
    url(r'^album/$', views.album, name='album'),
    url(r'^rest/piece/$',PieceListJson.as_view(), name='rest_piece_data'),
    url(r'^rest/album/$', AlbumListJson.as_view(), name='rest_album_data'),
)