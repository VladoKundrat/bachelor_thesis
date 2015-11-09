from django.contrib import admin
from .models import Piece, Album, Arrangement, PieceMovement, Interpret, Composer

class PieceAlbumInline(admin.TabularInline):
    model = Album.piece.through
    extra = 0

class ArrangementInline(admin.TabularInline):
    model = Arrangement
    extra = 0

class PieceMovementInline(admin.TabularInline):
    model = PieceMovement
    extra = 0

class InterpretPieceInline(admin.TabularInline):
    model = Interpret.piece.through
    extra = 0


class ComposerAlbumInline(admin.TabularInline):
    model = Composer.album.through
    extra = 0

class PieceAdmin(admin.ModelAdmin):
#   pass
    inlines =  [ArrangementInline, PieceMovementInline, PieceAlbumInline,]

    list_display = ('piece_id', 'cz_title', 'en_title', 'jw_catalogue_number_part_I', 'jw_catalogue_number_part_II', 'time_of_composition','date_of_premiere', 'place_of_premiere', 'compose_for', 'number_of_movement', 'wiki')

class AlbumAdmin(admin.ModelAdmin):

    inlines = [PieceAlbumInline, ComposerAlbumInline, ]
    exclude = ('piece',)
    list_display = ('album_id', 'label_name', 'catalogue_number', 'album_name', 'album_published_year', 'published_country', 'number_of_media', 'recording_technology', 'diameter', 'rpm', 'region_code', 'side_coumpling', 'tv_system', 'sound_system', 'medium_type', 'subtitles', 'comment', 'text_language', 'text_by', 'note_language', 'note_by', 'libretto_language', 'libretto_by')

class ArrangementAdmin(admin.ModelAdmin):

    list_display = ('arrangement_id', 'suitable_for', 'arrangemet_for', 'arrangemet_by', 'perfomr_by', 'piece_id')

class PieceMovementAdmin(admin.ModelAdmin):

    list_display = ('piece_movement_id', 'movement_order', 'movement_title', 'piece_id')

class InterpretAdmin(admin.ModelAdmin):

    inlines = [InterpretPieceInline, ]
    list_display = ('id', 'interpret_name')

class ComposerAdmin(admin.ModelAdmin):

    inlines = [ComposerAlbumInline, ]
    list_display = ('id', 'composer_name')



admin.site.register(Piece, PieceAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Arrangement, ArrangementAdmin)
admin.site.register(PieceMovement, PieceMovementAdmin)
admin.site.register(Interpret, InterpretAdmin)
admin.site.register(Composer, ComposerAdmin)



