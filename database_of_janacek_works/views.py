from django.shortcuts import render, render_to_response
from django_datatables_view.base_datatable_view import BaseDatatableView
from database_of_janacek_works.models import Piece, Album


def piece(request):
    return render_to_response('database_of_janacek_works/piece.html')

def album(request):
    return render_to_response('database_of_janacek_works/album.html')

class PieceListJson(BaseDatatableView):

        # The model we're going to show
       model = Piece

        # define the columns that will be returned
       columns = ['cz_title', 'en_title', 'jw_catalogue_number', 'time_of_composition', 'date_of_premiere', 'place_of_premiere', 'compose_for', 'number_of_movement', 'wiki']

        # define column names that will be used in sorting
       order_columns = ['cz_title', 'en_title', 'jw_catalogue_number_part_I', 'jw_catalogue_number_part_II', 'time_of_composition', 'date_of_premiere', 'place_of_premiere', 'compose_for', 'number_of_movement', 'wiki']

        # set max limit of records returned, this is used to protect our site if someone tries to attack our site and make it return huge amount of data
       max_display_length = 300

       def render_column(self, row, column):
            # We want to render jw_catalogue_number as a custom column
            if column == 'jw_catalogue_number':
                return '{0} / {1}'.format(row.jw_catalogue_number_part_I, row.jw_catalogue_number_part_II)
            elif column == 'jw_catalogue_number_part_II':
                return ()
            else:
                return super(PieceListJson, self).render_column(row, column)


class AlbumListJson(BaseDatatableView):

    # The model we're going to show
       model = Album

       # define the columns that will be returned
       columns = ['label_name', 'catalogue_number', 'album_name', 'album_published_year', 'published_country', 'number_of_media', 'recording_technology', 'side_coumpling', 'diameter', 'rpm',
                  'tv_system', 'region_code', 'sound_system', 'medium_type', 'comment', 'subtitles', 'text_language', 'text_by', 'note_language', 'note_by', 'libretto_language', 'libretto_by']

       # define column names that will be used in sorting
       order_columns = ['label_name', 'catalogue_number', 'album_name', 'album_published_year', 'published_country', 'number_of_media', 'recording_technology', 'side_coumpling', 'diameter', 'rpm',
                        'tv_system', 'region_code', 'sound_system', 'medium_type', 'comment', 'subtitles', 'text_language', 'text_by', 'note_language', 'note_by', 'libretto_language', 'libretto_by']
       # set max limit of records returned, this is used to protect our site if someone tries to attack our site and make it return huge amount of data
       max_display_length = 5000