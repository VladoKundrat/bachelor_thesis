from django.conf.urls import url, patterns
from . import views
from database_of_janacek_works.views import PieceListRenderer, AlbumListRenderer, ArrangementListRenderer, MovementListRenderer

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^piece/$', PieceListRenderer.as_view(), name='piece_list'),
    url(r'^album/$', AlbumListRenderer.as_view(), name='album_list'),
    url(r'^arrangement/$', ArrangementListRenderer.as_view(), name='arrangement_list'),
    url(r'^movement/$', MovementListRenderer.as_view(), name='movement_list')
)