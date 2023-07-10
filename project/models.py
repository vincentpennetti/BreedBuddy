# filename: models.py
# author: Vincent Pennetti (vpennett@bu.edu)
# description: django models definition



from django.db import models

from django.urls import reverse # to obtain a url from pattern name
from django.shortcuts import get_object_or_404

# Create your models here.
from datetime import datetime
from django.utils.timezone import now



class Plant(models.Model):
    """ Encapsulate the idea of a plant (i.e., text)."""

    # data attributes of a plant:
    name = models.CharField('Plant Name', default="", blank=True, max_length=100)
    monicker = models.CharField('Monicker', default="", blank=True, max_length=100)
    mother_name = models.CharField('Mother\'s Name', default="", blank=True, max_length=100)
    father_name = models.CharField('Father\'s Name', default="", blank=True, max_length=100)
    date_bred = models.DateField('Date Bred', blank=True, null=True)
    date_harvested = models.DateField('Date Harvested', blank=True, null=True)
    date_planted = models.DateField('Date Planted', blank=True, null=True)
    genus = models.CharField('Genus', default="", blank=True,  max_length=100)
    species = models.CharField('Species', default="", blank=True, max_length=100)
    current_location = models.CharField('Current Location', max_length=250, default="", blank=True)
    is_alive = models.BooleanField('Alive?', default=True)

    pheno_flower_red = models.BooleanField('Red Flower', default=False)
    pheno_flower_pink = models.BooleanField('Pink Flower', default=False)
    pheno_flower_blush = models.BooleanField('Blush Flower', default=False)
    pheno_flower_white = models.BooleanField('White Flower', default=False)
    pheno_flower_morphology = models.BooleanField('Generic', default=True)

    pheno_leaf_recessive = models.BooleanField('Green Leaf (vv)', default=False)

    pheno_leaf_whiteV = models.BooleanField('White V (V/_)', default=False)
    pheno_leaf_whiteVHigh = models.BooleanField('White V High (Vh/_)', default=False)
    pheno_leaf_whiteVIntermediate = models.BooleanField('White V Intermediate (Vi/_)', default=False)
    pheno_leaf_whiteVLow = models.BooleanField('White V Low (Vl/_)', default=False)
    pheno_leaf_brokenV = models.BooleanField('Broken V (Vb)', default=False)
    pheno_leaf_vPoint = models.BooleanField('V Point (Vp)', default=False)
    pheno_leaf_basal = models.BooleanField('Basal (VL)', default=False)
    pheno_leaf_filledV = models.BooleanField('Filled V (Vf/_)', default=False)
    pheno_leaf_brokenVyel = models.BooleanField('Broken V yellow tip (Vby)', default=False)

    pheno_leaf_red = models.BooleanField('Red leaf (Rl)', default=False)
    pheno_leaf_redSpot = models.BooleanField('Red Spot (Vr2)', default=False)
    pheno_leaf_redLeaflet = models.BooleanField('Red leaflet (Vrl)', default=False)
    pheno_leaf_redMidrib = models.BooleanField('Red Midrib (Rm)', default=False)
    pheno_leaf_redFleck = models.BooleanField('Red Fleck (Rf)', default=False)

    pheno_leaf_marginalMark = models.BooleanField('Marginal Mark (Vm)', default=False)
    pheno_leaf_halo = models.BooleanField('Halo (Vh2)', default=False)

    pheno_leaf_multifoliate = models.BooleanField('Multifoliate', default=False)
    pheno_leaf_trifoliate = models.BooleanField('Trifoliate', default=False)
    pheno_leaf_pinnate = models.BooleanField('Pinnate leaf', default=False)
    pheno_leaf_palmate = models.BooleanField('Palmate leaf', default=False)
    pheno_leaf_elongatedPetiole = models.BooleanField('Elongated Petiole', default=False)


    pheno_cyanogenic_gluc = models.BooleanField('Cyanogenic Glucosides (Ac)', default=False)
    pheno_cyanogenic_enzyme = models.BooleanField('Linamarase (Li)', default=False)

    pheno_compat = models.BooleanField('Self incompatible', default=True)


    def __str__(self):
        """Return a string representation of this object."""
        return self.name


    # get all images
    def get_all_images(self):
        """return a QuerySet of all images for this plant object."""
        # get all images of this person
        images = Image.objects.filter(plant=self.pk)
        return images

    # set profile picture
    # def set_profile_image(self, profpic_pk):
    #     """return a QuerySet of all images for this plant object."""
    #     # get all images of this person
    #     images = Image.objects.filter(plant=self.pk)
        
    #     # loop through the image set the new main image
    #     for image in images:
    #         if image.image_main == True:
    #             image.image_main = False

    #     print(images.filter(pk=profpic_pk).first().image_main)
    #     img_obj = images.filter(pk=profpic_pk).first().image_main 
    #     img_obj = True
    #     print(images.filter(pk=profpic_pk).first().image_main)
    #     return 

    # get all notes
    def get_all_notes(self):
        """return a QuerySet of all notes for this plant object."""
        # get all images of this person
        notes = Note.objects.filter(plant=self.pk)
        return notes
    

    # obtain the mother plant object
    def get_mother(self):
        """returns the mother object"""

        # use try/except to attempt parent retrieval
        try:
            return Plant.objects.get(name=self.mother_name)

        # handle the case of the parent not being in the database
        except Plant.DoesNotExist:
            return self


    # obtain the father plant object
    def get_father(self):
        """returns the father object"""

        # use try/except to attempt parent retrieval
        try:
            return Plant.objects.get(name=self.father_name)

        # handle the case of the parent not being in the database
        except Plant.DoesNotExist:
            return self


    # get the main image for the plant object
    def get_main_image(self):
        """returns the display image for the plant"""

        # get all the images for the plant
        image_obj = Image.objects.filter(plant=self.pk)


        # if there is a main image for the plant, get it and display it
        if image_obj.filter(image_main=True):
            image_obj = image_obj.filter(image_main=True).first()
            
            try:
                return image_obj.image_file.url

            except:
                return image_obj.image_url
        
        # if there is no main image declared, but there are images for the plant, display the first image
        elif image_obj.first():
            image_obj = image_obj.first()

            try:
                return image_obj.image_file.url

            except:
                return image_obj.image_url

        # if there are no images for the plant, default to wall-e
        else:
            return 'https://i.imgur.com/COfAjev.png'



    # get the pk of the main image, useful in the html templates
    def get_main_image_pk(self):
        """returns the pk of the display image for the plant"""
        
        # if there is a main image, get the pk
        try:
            image_pk = Image.objects.filter(plantID=self.pk).first().pk
            return image_pk
        
        # if there is no main image, return false
        except:
            return False
    

    # get the absolute plant url
    def get_absolute_url(self):
        """Return a URL to display this profile object."""
        return reverse("display_plant", kwargs={"pk":self.pk})


    # get a queryset of all the children on the maternal side
    def get_children_maternal(self):
        """Returns a queryset of all the plant's children where this plant is the mother"""
        return Plant.objects.filter(mother_name=self.name)


    # get a queryset of all the children on the paternal side
    def get_children_paternal(self):
        """Returns a queryset of all the plant's children where this plant is the father"""
        return Plant.objects.filter(father_name=self.name)


# model for the log book notes
class Note(models.Model):
    """ Encapsulate the idea of a note (i.e., text)."""

    # data attributes of a quote:
    text = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=now, editable=False)
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE) # CASCADE--if the plant is deleted, the notes will be deleted as well

    def __str__(self):
        """Return a string representation of this object."""
        return '%s: %s' % (self.timestamp, self.text)


# model for the images for plants
class Image(models.Model):
    """Represent an image, which is associated with a Plant."""
    
    # declare fields for both uploaded images and urls to images
    image_url = models.URLField(blank=True, null=True)
    image_file = models.ImageField(blank=True, null=True) # an actual image
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE) # CASCADE--if the plant is deleted, all the images associated with that plant will be deleted as well

    image_main = models.BooleanField('Main image?', default=False)

    # string representation adjusting for type of image loaded in the object
    def __str__(self):
        """Return a string representation of this image."""
        
        # if it is a url to an image
        if self.image_url:
            return '%s' % (self.image_url)
        
        # if it is an uploaded image
        else:
            return self.image_file.name

    
