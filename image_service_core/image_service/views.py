from django.shortcuts import render, redirect

from django.views.generic import View
from django.shortcuts import get_object_or_404

from .forms import *
from .models import *


def images_list(request):
    images = Image.objects.all()
    return render(request, 'image_service/index.html', context={'images': images})
    
class ImageUpload(View):
    def get(self, request):
        form = ImageForm()
        return render(request, 'image_service/image_upload.html', context={'form': form})
    
    def post(self, request):
        bound_form = ImageForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_image = bound_form.save()
            return redirect(new_image)
        return render(request, 'image_service/image_upload.html', context={'form': bound_form})

class ImageEdit(View):
    def get(self, request, title):
        image = get_object_or_404(Image, title = title)
        bound_form = ImageEditForm(instance=image)
        return render(request, 'image_service/image_edit.html', context={'form': bound_form, 'image': image})

    def post(self, request, title):
        image = get_object_or_404(Image, title = title)
        bound_form = ImageEditForm(request.POST, request.FILES, instance=image)
        if bound_form.is_valid():
            new_image = bound_form.save()
            return redirect(new_image.get_absolute_url())
        return render(request, 'image_service/image_edit.html', context={'form': bound_form, 'image': image})


