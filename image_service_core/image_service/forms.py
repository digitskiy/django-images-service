from django import forms
from .models import *

from django.core.exceptions import ValidationError

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image_url', 'image_file')

    def clean(self):
        new_image_file = self.cleaned_data.get('image_file')
        new_image_url = self.cleaned_data.get('image_url')
        # Если ни одно из полей формы не было заполнено или были заполнены оба
        if ( not new_image_file and not new_image_url):
            raise ValidationError("Должно быть заполнено хотя бы одно из двух полей!")
        if (new_image_file and new_image_url):
            raise ValidationError("Должно быть заполнено только одно из двух полей!")
        # Получаем title изображения
        if new_image_file and hasattr(new_image_file, 'name'):
            new_title = new_image_file.name
        elif new_image_url:
            new_title = os.path.basename(new_image_url)
        # Если в БД уже есть изображение с таким title
        if Image.objects.filter(title=new_title).count():
            raise ValidationError("Изображение должно быть уникальным!")
        return self.cleaned_data

class ImageEditForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('width', 'height')
    
    def clean(self):
        width = self.cleaned_data.get('width')
        height = self.cleaned_data.get('height')
        # Если ни одно из полей формы не было заполнено
        if (not width) and (not height ):
            raise ValidationError("Должно быть заполнено хотя-бы одно из двух полей!")
        return self.cleaned_data
