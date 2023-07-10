# filename: resources.py
# author: Vincent Pennetti (vpennett@bu.edu)
# description: django resources file for the import_export module


from import_export import resources
from .models import Plant, Image, Note

# this file enables the use of django import_export for easier backend management of the data

class PlantResource(resources.ModelResource):
    """"""
    class Meta:
        model = Plant

class ImageResource(resources.ModelResource):
    """"""
    class Meta:
        model = Image

class NoteResource(resources.ModelResource):
    """"""
    class Meta:
        model = Note