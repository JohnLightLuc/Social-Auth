# Social-Auth
 Social authentification
 
 Installation 
    
    pip install django-allauth
    
Documentation
    
    #Django-allauth
    https://django-allauth.readthedocs.io/en/latest/installation.html
    
    #django-social-auth
    https://github.com/python-social-auth/social-app-django
    https://python-social-auth.readthedocs.io/en/latest/configuration/django.html

Guide

    https://www.youtube.com/watch?v=dXZim_jgaiI&t=334s
    
## Configuration facebook

1- Installation
    
    django-extensions==2.2.5
    django-werkzeug==1.0.0
    pyOpenSSL==19.0.0
    Werkzeug==0.16.0
    
2- Install App

     INSTALLED_APPS = (
     ...
     'django_extensions',
     ...
    )
    
3- Ajout du fichier certname.key et certname.crt dans le projet

4- Lancer la comande suivante

    python manage.py runserver_plus --cert certname
   
