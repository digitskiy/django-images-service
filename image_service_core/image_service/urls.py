
from django.urls import path
from .views import *

urlpatterns = [
    path('', images_list, name='images_list_url'),
    path('image/upload/', ImageUpload.as_view(), name='image_upload_url'),
    path('image/edit/<str:title>', ImageEdit.as_view(), name='image_edit_url'),
]

