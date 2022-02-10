# Importing a function to redirect requests
from django.shortcuts import redirect

# Handler function to redirect the request from the main page to the page with the image '/images'
def redirect_images(request):
    # permanent=True - permanent redirect 
    return redirect('images_list_url', permanent=True)
