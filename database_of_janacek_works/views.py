from django.http import HttpResponse

from database_of_janacek_works.static.datatableview.views import DatatableView
from database_of_janacek_works.models import Piece


def index(request):
    return HttpResponse("Hello world")

class PieceListRenderer(DatatableView):

    # The model we're going to show
    model = Piece