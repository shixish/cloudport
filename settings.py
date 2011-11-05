# Django settings for cloudport project.
from base_settings import * #imports the sensitive settings

DEBUG = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'cloudport.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/var/www-django/cloudport/templates/",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    #'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #'django.contrib.staticfiles', #only available since 1.3
    'djangorestframework', #i installed this library using "sudo pip install djangorestframework"
    'cloudport.polls',
    'cloudport.job_manager',
    'cloudport.default',
    'cloudport.templates', #needed to do this to make the templatetags work...
)

TASK_UPLOAD_FILE_EXTENSIONS = ['sce']
#TASK_UPLOAD_FILE_TYPES = ['pdf', 'vnd.oasis.opendocument.text','vnd.ms-excel','msword','application',]
TASK_UPLOAD_FILE_MAX_SIZE = "5242880"
