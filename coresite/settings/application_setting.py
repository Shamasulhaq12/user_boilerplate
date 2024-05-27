DJANGO_APPLICATIONS = [
    'django.contrib.auth',
    "admin_interface",
    'storages',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.sessions',
    "daphne",
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',

]

CUSTOM_APPLICATIONS = [
    'apps.core.apps.CoreConfig',
    'apps.userprofile.apps.UserprofileConfig',
]

THIRD_PARTY_APPLICATIONS = [

    'drf_yasg',
    'corsheaders',
    'rest_framework',
]
