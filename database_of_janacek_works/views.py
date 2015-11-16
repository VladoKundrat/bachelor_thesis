from django.http import HttpResponse

from database_of_janacek_works.static.datatableview.views import DatatableView
from database_of_janacek_works.models import Piece, Album


def index(request):
    return HttpResponse("Hello world")

class PieceListRenderer(DatatableView):

    # The model we're going to show
    model = Piece

    datatable_options = {
        'columns': [
            'piece_id',
            'cz_title',
            'en_title',
            ("catalogue number", ['jw_catalogue_number_part_I', 'jw_catalogue_number_part_II'], 'get_catalogue_number'),
            'time_of_composition',
            'date_of_premiere',
            'place_of_premiere',
            'compose_for',
            'number_of_movement',
            'wiki'
        ],
        'hidden_columns': ['piece_id', 'compose_for', 'number_of_movement', 'wiki'],
    }

    def get_catalogue_number(self, instance, *args, **kwargs):
        return "%s / %s" % (instance.jw_catalogue_number_part_I, instance.jw_catalogue_number_part_II)

class AlbumListRenderer(DatatableView):

    model = Album