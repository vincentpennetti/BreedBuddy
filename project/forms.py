# filename: forms.py
# author: Vincent Pennetti (vpennett@bu.edu)
# description: django forms file for declaring user input forms

from django import forms
from .models import *
from django.urls import reverse_lazy
from django.urls import reverse # to obtain a url from pattern name



class AddPlantForm(forms.ModelForm):
    """A form to add new plants to the database."""

    # explicit form field definition
    date_bred = forms.DateField(widget=forms.SelectDateWidget(years=range(2020,1900,-1),), required=False)
    date_harvested = forms.DateField(widget=forms.SelectDateWidget(years=range(2020,1900,-1),), required=False)
    date_planted = forms.DateField(widget=forms.SelectDateWidget(years=range(2020,1900,-1),), required=False)


    class Meta:
        """Associate this form with the Plant Model."""
        model = Plant
        fields = ['name',
                    'monicker',
                    'mother_name',
                    'father_name',
                    'date_bred',
                    'date_harvested',
                    'date_planted',
                    'genus',
                    'species',
                    'current_location',
                    'is_alive',
                    'pheno_flower_red',
                    'pheno_flower_pink',
                    'pheno_flower_blush',
                    'pheno_flower_white',
                    'pheno_flower_morphology',
                    'pheno_leaf_recessive',
                    'pheno_leaf_whiteV',
                    'pheno_leaf_whiteVHigh',
                    'pheno_leaf_whiteVIntermediate',
                    'pheno_leaf_whiteVLow',
                    'pheno_leaf_brokenV',
                    'pheno_leaf_vPoint',
                    'pheno_leaf_basal',
                    'pheno_leaf_filledV',
                    'pheno_leaf_brokenVyel',
                    'pheno_leaf_red',
                    'pheno_leaf_redSpot',
                    'pheno_leaf_redLeaflet',
                    'pheno_leaf_redMidrib',
                    'pheno_leaf_redFleck',
                    'pheno_leaf_marginalMark',
                    'pheno_leaf_halo',
                    'pheno_leaf_multifoliate',
                    'pheno_leaf_trifoliate',
                    'pheno_leaf_pinnate',
                    'pheno_leaf_palmate',
                    'pheno_leaf_elongatedPetiole',
                    'pheno_cyanogenic_gluc',
                    'pheno_cyanogenic_enzyme',
                    'pheno_compat']

class UpdatePlantForm(forms.ModelForm):
    """A form to update plant entries in the database."""

    # explicit form field definition
    date_bred = forms.DateField(widget=forms.SelectDateWidget(years=range(2020,1900,-1),), required=False)
    date_harvested = forms.DateField(widget=forms.SelectDateWidget(years=range(2020,1900,-1),), required=False)
    date_planted = forms.DateField(widget=forms.SelectDateWidget(years=range(2020,1900,-1),), required=False)


    class Meta:
        """Associate this form with the Plant Model."""
        model = Plant
        fields = ['name',
                        'monicker',
                        'mother_name',
                        'father_name',
                        'date_bred',
                        'date_harvested',
                        'date_planted',
                        'genus',
                        'species',
                        'current_location',
                        'is_alive',
                        'pheno_flower_red',
                        'pheno_flower_pink',
                        'pheno_flower_blush',
                        'pheno_flower_white',
                        'pheno_flower_morphology',
                        'pheno_leaf_recessive',
                        'pheno_leaf_whiteV',
                        'pheno_leaf_whiteVHigh',
                        'pheno_leaf_whiteVIntermediate',
                        'pheno_leaf_whiteVLow',
                        'pheno_leaf_brokenV',
                        'pheno_leaf_vPoint',
                        'pheno_leaf_basal',
                        'pheno_leaf_filledV',
                        'pheno_leaf_brokenVyel',
                        'pheno_leaf_red',
                        'pheno_leaf_redSpot',
                        'pheno_leaf_redLeaflet',
                        'pheno_leaf_redMidrib',
                        'pheno_leaf_redFleck',
                        'pheno_leaf_marginalMark',
                        'pheno_leaf_halo',
                        'pheno_leaf_multifoliate',
                        'pheno_leaf_trifoliate',
                        'pheno_leaf_pinnate',
                        'pheno_leaf_palmate',
                        'pheno_leaf_elongatedPetiole',
                        'pheno_cyanogenic_gluc',
                        'pheno_cyanogenic_enzyme',
                        'pheno_compat']


class AddImageForm(forms.ModelForm):
    """A form to collect an image from the user."""
   
    # explicit form field definition
    image_file = forms.ImageField(required=False)
    
    class Meta:
        model = Image
        fields = ["image_file", "image_url", "image_main"]

class SetProfileImageForm(forms.ModelForm):
    """A form to set profile image."""
    image_main = forms.BooleanField(required=True)

    class Meta:
        model = Image
        fields = ["image_main",]


# class SortForm(forms.ModelForm):
#     """ A form for sorting the displayed plants """

#     class Meta:
#         CHOICES = (('name', 'Name (ascending)'),('-name', 'Name (descending)'),('monicker', 'Monicker (ascending)'),('-monicker', 'Monicker (descending)'),('date_bred', 'Date Bred'),('-is_alive', 'Presence'),)
#         field = forms.ChoiceField(choices=CHOICES)



    

