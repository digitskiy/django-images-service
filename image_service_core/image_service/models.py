from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.shortcuts import reverse

from io import BytesIO
from PIL import Image as Img
import requests
from requests.exceptions import RequestException
import os
from django.core.files.storage import FileSystemStorage 


class OverwriteStorage(FileSystemStorage):
    """ Overwriting a modified image file in case such a file already exists """
    def get_available_name(self, name, *args, **kwargs):
        self.delete(name)
        return name

def validate_image_url(url):
    """ Validator to check if an image file exists in a URL link """
    # Execute the request and check the content type of the response payload using the 'Content-Type' header
    with requests.get(url, stream=True) as response:
        content_type = response.headers.get('Content-Type')
        if content_type and content_type.split('/')[0] != 'image':
            raise ValidationError("Данная ссылка не содержит изображения!")
    # Trying to open a file to make sure it's a real image
        img_file = ContentFile(response.content)
        try:
            with Img.open(img_file) as img:
                img.verify()
        except Exception:
            raise ValidationError("Данная ссылка не содержит изображения!")

class Image(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image_file = models.ImageField(
        upload_to='images/',
        verbose_name='Файл',
        blank=True,
        null=True)
    image_url = models.URLField(
        max_length=255, 
        verbose_name='Ссылка', 
        blank=True, null=True, 
        validators=[validate_image_url])
    image_file_resized = models.ImageField(
        upload_to='images/resized/',
        storage=OverwriteStorage(),
        verbose_name='Файл',
        blank=True, 
        null=True)
    width = models.PositiveIntegerField(
        default=0, 
        blank=True, 
        verbose_name='Ширина', 
        validators=[MinValueValidator(100), MaxValueValidator(10000)])
    height = models.PositiveIntegerField(
        default=0, 
        blank=True, 
        verbose_name='Высота',
        validators=[MinValueValidator(100), MaxValueValidator(10000)])
    date_upload = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Generating a link to a specific image """
        return reverse('image_edit_url', kwargs={'title': self.title})

    def get_remote_image(self):
        """ Downloading the image file received from the link """
        try:
            response = requests.get(self.image_url)
            response.raise_for_status()
        except RequestException as r_err:
            print(f'Произошла ошибка запроса: {r_err}')
        except Exception as err:
            print(f'Произошла другая ошибка: {err}')
        else:
            return response
    
    def save_remote_image(self):
        """ Saving an image file received from a link """
        if self.image_url and not self.image_file:
            fname = os.path.basename(self.image_url)
            resp = self.get_remote_image()
            self.image_file.save(fname, ContentFile(resp.content), save=False)
    
    def resize_image(self):
        """ Resizing an image and saving a resized copy """
        # Determine the path and name of the file
        fname, _ext = os.path.splitext(self.title)
        fcopy = f"{fname}_copy{_ext}"
        image = self.image_file
        # Determining the dimensions of the image
        width = self.width or self.height
        height = self.height or self.width
        size = (width, height)
        # Open file in old path, resize and save in new path
        try:
            with Img.open(image) as img:
                img.thumbnail(size, Img.ANTIALIAS)
                temp_img = BytesIO()
                img.save(fp=temp_img, format=img.format)
                temp_img.seek(0)
                temp_img_value = temp_img.getvalue()
                self.image_file_resized.save(fcopy, ContentFile(temp_img_value), save=False)
                temp_img.close()
        except FileNotFoundError:
            print("Файл с изображением не найден!")        

    def save(self, *args, **kwargs):
        # If the object is not yet in the database
        if not self.id:
            # If the title attribute is not yet defined, then we determine depending on where the image was loaded from
            if not self.title:
                self.title = self.image_file.name or os.path.basename(self.image_url)  
            self.save_remote_image() 
            # If one of the width and/or height attributes is empty, then assign the width and height of the original image
            if not self.width:
                self.width = self.image_file.width
            if not self.height:
                self.height = self.image_file.height        
        else:
            self.resize_image()
            # Assign the width and height of the resized image to the width and height properties
            self.width = self.image_file_resized.width
            self.height = self.image_file_resized.height
        super(Image, self).save(*args, **kwargs)


    
    
