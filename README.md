# django-images-service
Django web service for loading images and resizing them 

This web service allows:
- Upload images from the user's computer or by URL
- Resize images
- Save both original and modified images to the database
- Viewing a list of images with basic information


## Installation
1. git clone <https://github.com/IniSlice/django-images-service.git>
2. Install virtual environment: $ python -m venv myenv
3. Activate virtual environment:
for Windows $ myenv\Scripts\activate
for Linux $ source myenv/bin/activate
5. Install requirements: (myenv) $ pip install -r requirements.txt
6. Run all migrations: (myenv) $ python manage.py makemigrations, $ python manage.py migrate
7. Start local server Django: (myenv) $ python manage.py runserver
