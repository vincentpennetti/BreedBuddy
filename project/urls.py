# file: project/urls.py
# author: Vincent Pennetti (vpennett@bu.edu)
# description: direct URL requests to view functions

from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

# all of the url patterns for this particular project
urlpatterns=[
    path('', ExtantPlantView.as_view(), name='extant'),
    path('all/', ShowAllPlantsView.as_view(), name='show_all_plants'),
    path('plant/<int:pk>', ShowIndividualPlantView.as_view(), name='display_plant'),
    path('add', login_required(AddPlantView.as_view()), name='add_new_plant'),
    path('plant/<int:pk>/update', login_required(UpdatePlantView.as_view()), name='update_plant'),
    path('plant/<int:pk>/post_note', create_note, name='post_note'),
    path('plant/<int:pk>/add', add_new_image, name='add_new_image'),
    path('plant/<int:pk>/gallery', PlantImageGalleryView.as_view(), name='gallery'),
    path('plant/<int:plant_pk>/single_image/<int:image_pk>', SingleImageView.as_view(), name="single_image"),
    path('plant/<int:plant_pk>/delete_image/<int:image_pk>', login_required(DeleteImageView.as_view()), name="delete_image"),
    path('plant/<int:pk>/log', LogBookView.as_view(), name='logbook'),
    path('in_memoriam/', InMemoriamView.as_view(), name='all_dead_plants'),
    path('labplants/', LabPlantView.as_view(), name='all_lab_plants'),
    path('VinnysClovers/', PersonalPlantView.as_view(), name='all_personal_plants'),
    path('plant/<int:plant_pk>/set_profile_image/<int:image_pk>/', set_profile_image, name='set_profile_image'),


]