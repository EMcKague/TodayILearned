References: 
https://docs.python.org/3/library/venv.html
https://docs.djangoproject.com/en/3.2/intro/tutorial01/


Django Project notes
in settings.py, you must declare your templates folder like so: 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
    
When declaring a model (class) make sure it inherits from models.Model

Everytime a change is made to a model, you must run the following: 
python manage.py makemigrations
python manage.py migrate

Opening an interactive shell with python: 
python manage.py shell

Launch Application
cd blog_env 
Scripts\Activate.bat
cd .. 
cd TodayILearned
python manage.py runserver