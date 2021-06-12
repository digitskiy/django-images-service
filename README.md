# django-images-service
Веб-сервис Django для загрузки изображений и изменения их размеров

Данный веб-сервис позволяет:
- Загружать изображения с компьютера пользователя или по URL
- Изменять размер изображений
- Сохранять как оригинальные, так и измененные изображения в базу данных
- Просматривать список изображений с основной информацией


## Установка
1. git clone <https://github.com/IniSlice/django-images-service.git>
2. Установить виртуальное окружение: $ python -m venv myenv
3. Активировать виртуальное окружение: для Windows $ myenv\Scripts\activate или для Linux $ source myenv/bin/activate
4. Установить зависимости: $ pip install -r requirements.txt
5. Провести миграции: $ python manage.py makemigrations, $ python manage.py migrate
6. Запустить локальный сервер Django: $ python manage.py runserver
