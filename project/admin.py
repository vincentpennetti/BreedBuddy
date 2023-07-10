from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Plant, Image, Note

#admin.site.register(Plant)
#admin.site.register(Image)
#admin.site.register(Note)


# register the models appropriately for import_export module
@admin.register(Plant)
class PlantAdmin(ImportExportModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(ImportExportModelAdmin):
    pass

@admin.register(Note)
class NoteAdmin(ImportExportModelAdmin):
    pass