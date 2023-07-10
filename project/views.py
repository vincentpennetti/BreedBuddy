# filename: views.py
# author: Vincent Pennetti (vpennett@bu.edu)
# description: django views file for displaying webpage


from django.shortcuts import render

# Create your views here.
from .models import Plant
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView, DeleteView
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# listview based view for displaying all of the plants
class ShowAllPlantsView(ListView):
    """Create a subclass of ListView to display all plants."""

    model = Plant # retrieve objects of type Quote from the database
    template_name = 'project/show_all_plants.html'
    context_object_name = 'all_plants_list' # how to find the data in the template file

 #   def get_queryset(self):
 #       return Plant.objects.order_by('name') # organize the plants by name

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'name')
        new_context = Plant.objects.order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(ShowAllPlantsView, self).get_context_data(**kwargs)
        context['orderby'] = self.request.GET.get('orderby', 'name')
        return context
        
class InMemoriamView(ListView):
    model = Plant # retrieve objects of type Quote from the database
    template_name = 'project/in_memoriam.html'
    context_object_name = 'all_plants_list' # how to find the data in the template file

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'name')
        new_context = Plant.objects.filter(is_alive=False).order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(InMemoriamView, self).get_context_data(**kwargs)
        context['orderby'] = self.request.GET.get('orderby', 'name')
        return context

class ExtantPlantView(ListView):
    model = Plant # retrieve objects of type Quote from the database
    template_name = 'project/extant.html'
    context_object_name = 'all_plants_list' # how to find the data in the template file

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'name')
        new_context = Plant.objects.filter(is_alive=True).order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(ExtantPlantView, self).get_context_data(**kwargs)
        context['orderby'] = self.request.GET.get('orderby', 'name')
        return context

class LabPlantView(ListView):
    model = Plant # retrieve objects of type Quote from the database
    template_name = 'project/lab_plants.html'
    context_object_name = 'all_plants_list' # how to find the data in the template file

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'name')
        new_context = Plant.objects.filter(is_alive=True).filter(name__startswith="L-").order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(LabPlantView, self).get_context_data(**kwargs)
        context['orderby'] = self.request.GET.get('orderby', 'name')
        return context

class PersonalPlantView(ListView):
    model = Plant # retrieve objects of type Quote from the database
    template_name = 'project/personal_plants.html'
    context_object_name = 'all_plants_list' # how to find the data in the template file

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'name')
        new_context = Plant.objects.filter(is_alive=True).filter(name__startswith="P-").order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(PersonalPlantView, self).get_context_data(**kwargs)
        context['orderby'] = self.request.GET.get('orderby', 'name')
        return context


# detailview based view for displaying a particular plant's information
class ShowIndividualPlantView(DetailView):
    """Create a subclass of DetailView to display all plant info."""
    model = Plant
    template_name = "project/display_plant.html"
    context_object_name = "plant"


# a view for creating a new plant
class AddPlantView(CreateView):
    """A subclass of Createview to display the create plant functionality."""
    form_class = AddPlantForm
    template_name = "project/add_new_plant.html"  


# a view for updating a plant's info
class UpdatePlantView(UpdateView):
    """A subclass of Updateview to display the update plant functionality."""
    form_class = UpdatePlantForm
    template_name = "project/update_plant.html"
    queryset = Plant.objects.all()


# a view for displaying the logbook for a particular plant
class LogBookView(DetailView):
    """Create a subclass of DetailView to display all notes."""
    model = Plant
    template_name = "project/logbook.html"
    context_object_name = "plant"


# a view for displaying all of the images for a plant in a gallery-style
class PlantImageGalleryView(DetailView):
    """Create a subclass of Listview to display all images of a plant."""
    model = Plant
    template_name = 'project/gallery.html'
    context_object_name = 'plant'


# a view for displaying an individual image from a plant's gallery
class SingleImageView(DetailView):
    """ A view to see a single image."""
    template_name = "project/single_image.html"
    queryset = Image.objects.all()

    def get_context_data(self, **kwargs):
        """Return a dictionary with context data for this template to use."""
        # get the default context data:
        # this will include the Profile record for this page view
        context = super(SingleImageView, self).get_context_data(**kwargs)

        img = Image.objects.get(pk=self.kwargs['image_pk'])
        plnt = Image.objects.get(pk=self.kwargs['image_pk']).plant
        
        context['img'] = img
        context['plnt'] = plnt
        form = SetProfileImageForm()
        context['form'] = form

        # return the context dictionary
        return context
    
    def get_object(self):
        """Returns the Note Object that should be deleted."""
         # read the URL data values into variables
        plant_pk = self.kwargs['plant_pk']
        image_pk = self.kwargs['image_pk']

        # find the StatusMessage object, and return it
        return Image.objects.get(pk=image_pk)


# a view class for deleting an image
class DeleteImageView(DeleteView):
    """ A view to delete an image."""
    template_name = "project/delete_image_form.html"
    queryset = Image.objects.all()

    def get_context_data(self, **kwargs):
        """Return a dictionary with context data for this template to use."""
        # get the default context data:
        # this will include the Profile record for this page view
        context = super(DeleteImageView, self).get_context_data(**kwargs)

        img = Image.objects.get(pk=self.kwargs['image_pk'])

        context['img'] = img

        # return the context dictionary
        return context
    
    def get_object(self):
        """Returns the Image Object that should be deleted."""
         # read the URL data values into variables
        plant_pk = self.kwargs['plant_pk']
        image_pk = self.kwargs['image_pk']

        # find the StatusMessage object, and return it
        return Image.objects.get(pk=image_pk)

    def get_success_url(self):
        """Return to the URL to which we should be directed after the delete."""

        # get the pk for this image
        pk = self.kwargs.get('image_pk')
        # find the plant associated with the quote
        img = Image.objects.filter(pk=pk).first() # get one object from the QuerySet

        # reverse to show the gallery
        plant = img.plant

        return reverse('gallery', kwargs={'pk':plant.pk})

# a function based view for creating a note, behind a login wall
@login_required
def create_note(request, pk):
    '''
    Process a form submission to post a new status message.
    '''
    # find the plant that matches the `pk` in the URL
    plant = Plant.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        text = request.POST['text']

        # save the new note object to the database
        if text:

            nt = Note()
            nt.plant = plant
            nt.text = text
            nt.save()

    # redirect the user to the show_profile_page view
    return redirect(reverse('logbook', kwargs={'pk': pk}))


# a function based view for creating an image, behind a login wall
@login_required
def add_new_image(request, pk):
    """A custom view functino to handle the submission of an image upload."""
    # find the plant for whom we are submitting the image
    
    plant = Plant.objects.get(pk=pk)
    
    if request.method == 'POST':
        if "cancel" in request.POST:
            return redirect('display_plant', pk=plant.pk)
        # read request data into AddImageForm object
        form = AddImageForm(request.POST or None, request.FILES or None)
        
        # check if the form is valid, save object to database
        if form.is_valid():
            image = form.save(commit=False) # create the Image object, but not save
            
            if image.image_url:
                if (image.image_url[-4] != "." and image.image_url[-4:] not in [".jpg", ".JPG", ".png", ".PNG"]):
                    image.image_url += ".jpg"

            image.plant = plant
            image.save()
            return redirect('display_plant', pk=plant.pk)
    
    else:
        print("Error: the form was not valid.")
        image = AddImageForm()

    # redirect to a new URL, display person page
    return render(request, 'project/add_new_image.html', {'form':image})


@login_required
def set_profile_image(request, plant_pk, image_pk):
    """A custom view function to set profile image."""
    
    # find the plant for whom we are setting the image
    plant = Plant.objects.get(pk=plant_pk)

    if request.method == 'POST':
        if "cancel" in request.POST:
            return redirect('display_plant', pk=plant.pk)
        
        form = SetProfileImageForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            images = Image.objects.filter(plant=plant_pk)
        
            # loop through the image set the new main image
            for image in images:
                image.image_main = False
                image.save()

            newprofimage = images.filter(pk=image_pk).first()
            newprofimage.image_main = True
            newprofimage.save()

            return redirect('display_plant', pk=plant.pk)
    
        else:
            print("Error: the form was not valid.")
    else:
        return reverse('gallery', kwargs={'pk':plant.pk})