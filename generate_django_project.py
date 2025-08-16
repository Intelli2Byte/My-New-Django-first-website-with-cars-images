import os
from pathlib import Path
import shutil

project_name = "mysite"
app_name = "main"
base_dir = Path("output") / project_name

# Define paths
app_dir = base_dir / app_name
templates_dir = base_dir / "templates"
static_dir = base_dir / "static"

# Create directory structure
(app_dir / "migrations").mkdir(parents=True, exist_ok=True)
templates_dir.mkdir(parents=True, exist_ok=True)
static_dir.mkdir(parents=True, exist_ok=True)

# manage.py
(base_dir / "manage.py").write_text(f"""#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{project_name}.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
""")

# settings.py
settings = f'''import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '{app_name}',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{project_name}.urls'

TEMPLATES = [
    {{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {{
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }},
    }},
]

WSGI_APPLICATION = '{project_name}.wsgi.application'

DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }}
}}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
'''
(base_dir / project_name).mkdir()
(base_dir / project_name / "settings.py").write_text(settings)

# urls.py (project)
(base_dir / project_name / "urls.py").write_text(f"""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('{app_name}.urls')),
]
""")

# wsgi.py
(base_dir / project_name / "wsgi.py").write_text(f"""import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')
application = get_wsgi_application()
""")

# app urls.py
(app_dir / "urls.py").write_text("""from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
""")

# app views.py
(app_dir / "views.py").write_text("""from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
""")

# HTML Template
(templates_dir / "home.html").write_text("""<!DOCTYPE html>
<html>
<head>
    <title>Simple Django Website</title>
    <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
</head>
<body>
    <h1>Welcome to My Simple Django Website!</h1>
    <p>This is a static page with no models.</p>
</body>
</html>
""")

# Static CSS
(static_dir / "style.css").write_text("""body {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
    text-align: center;
}
h1 {
    color: #333;
}
""")
