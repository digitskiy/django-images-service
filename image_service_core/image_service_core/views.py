# Импортируем функцию для перенаправления запросов
from django.shortcuts import redirect

# Функция обработчик для перенаправления запроса с главной страницы на страницу с изображениемя '/images'
def redirect_images(request):
    # permanent=True - постоянный редирект 
    return redirect('images_list_url', permanent=True)