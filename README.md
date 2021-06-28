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
   
# Package social-auth-app-django

## 1- Installation

    pip install social-auth-app-django
    

## 2- Add to install apps (Settings.py )

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles', 

        'social_django',  # <-- Here social-auth-app-django
    ]
    
## 3- Migration

    python manage.py migrate 
    
## Configuration

### Settings.py

#### MIDDLEWARE

    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',

        'social_django.middleware.SocialAuthExceptionMiddleware',  # <-- Here
    ]
 
 #### CONTEXT PROCESSORS
 
    TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [BASE_DIR + '/templates/',],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',

                   'social_django.context_processors.backends',  # <-- Here
                   'social_django.context_processors.login_redirect', # <-- Here
               ],
           },
       },
    ] 
    
#### Add AUTHENTICATION_BACKENDS

    AUTHENTICATION_BACKENDS = (
        'social_core.backends.facebook.FacebookOAuth2',
        'social_core.backends.twitter.TwitterOAuth',
        'social_core.backends.github.GithubOAuth2',

        'django.contrib.auth.backends.ModelBackend',
    )
#### Set URL redirection

    LOGIN_URL = 'login'
    LOGOUT_URL = 'logout'
    LOGIN_REDIRECT_URL = 'home'
    
#### SOCIAL NETWORKS

##### Facebook 

 1- Creating your app on https://developers.facebook.com and set ID and Secret Key
  
 2- Add redirection URI
 
   Products > Facebook Login > Paramètres > URI de redirection OAuth valides
    
           https://my-domain-name.com/oauth/complete/facebook/
           
  3- Complete in Settings.py

     SOCIAL_AUTH_FACEBOOK_KEY = 'my-app-key'  # App ID
     SOCIAL_AUTH_FACEBOOK_SECRET = 'my-app-secret'  # App Secret

##### Google 

 1- Creating your app on https://console.developers.google.com/ and set ID and Secret Key
  
 2- Add redirection URI
 
   Choose the app > Identifiants 
    Origines JavaScript autorisées (Liste des site autorisé)
    URI*
     
      http://localhost:8000
      
   URI de redirection autorisés
   URI*
     
     http://localhost:8000/oauth/complete/google-oauth2/
    
           
  3- Complete in Settings.py
     
     SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '851202459960-8eukhfo22b2vdu6bip8vrft9vsmnkktchg.apps.googleusercontent.com'
     SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'VUjkNo-ke_iAIxxli9jrTuOEr9'


### Urls.py
    
    from django.urls import path, include
    
    urlpatterns = [
        ....
        path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
    ]
    
 ### Template Form Add link to connect With Social Account
 
    {% url 'social:begin' 'facebook' %} ## Facebook
    {% url 'social:begin' 'google-oauth2' %} ## GOOGLE
    
