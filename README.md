# django-images-service
Веб-сервис Django для загрузки изображений и изменения их размеров

Данный веб-сервис позволяет:
- Загружать изображения с компьютера пользователя или по URL
- Сохранять загруженные изображения в базу данных SQLite
- Изменять размер изображений и при этом сохранять оригинальные изображения
- Просматривать как список изображений с подробной информацией, так и конкретные изображения


## Установка
1. git clone <https://github.com/IniSlice/django-images-service.git>
2. Установить виртуальное окружение: $ python -m venv myenv
3. Активировать виртуальное окружение: для Windows $ myenv\Scripts\activate или для Linux $ source myenv/bin/activate
4. Установить зависимости: $ pip install -r requirements.txt
5. Провести миграции: $ python manage.py makemigrations, $ python manage.py migrate
6. Запустить локальный сервер Django: $ python manage.py runserver
