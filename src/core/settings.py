import os
from pathlib import Path
from .env import env

BASE_DIR = Path(__file__).resolve().parent.parent

env.read_env(os.path.join(BASE_DIR.parent, ".env"))

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = [
    "warehouse.eu-north-1.elasticbeanstalk.com",
    "http://warehouse.eu-north-1.elasticbeanstalk.com/",
    "https://warehouse.eu-north-1.elasticbeanstalk.com/",

    "localhost",
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://warehouse.eu-north-1.elasticbeanstalk.com/",
    "https://warehouse.eu-north-1.elasticbeanstalk.com/",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "rest_framework",
    "uritemplate",
    "storages",
]

INSTALLED_EXTENSIONS = [
    "containers",
    "staff",
    "api",
    "crispy_forms",
    "crispy_bootstrap4",
]

INSTALLED_APPS += INSTALLED_EXTENSIONS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


if env("ENVIRONMENT") == "ci":
    """For ci use sqlite database"""
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "sqlite3.db",
        }
    }
else:
    USE_RDS = env("USE_RDS")
    if USE_RDS:
        """AWS RDS DB settings"""
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": env("RDS_DB_NAME"),
                "USER": env("RDS_USERNAME"),
                "PASSWORD": env("RDS_PASSWORD"),
                "HOST": env("RDS_HOSTNAME"),
                "PORT": "5432",
            }
        }
    else:
        """alt settings for local DB"""
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": env("NAME"),
                "USER": env("USER"),
                "PASSWORD": env("PASSWORD"),
                "HOST": env("HOST"),
                "PORT": "5432",
            }
        }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"


LOGIN_REDIRECT_URL = "main-page"
LOGOUT_REDIRECT_URL = "login"
LOGIN_URL = "login"

AUTH_USER_MODEL = "staff.StaffModel"


"""sending email settings"""

"""sending email from server"""
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_USE_TLS = True
EMAIL_PORT = 587

if (
    env("EMAIL_HOST_USER") is None
    and env("EMAIL_HOST_PASSWORD") is None
    and env("DEFAULT_FROM_EMAIL") is None
):
    """sending emails to app"""
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = BASE_DIR / "sent_emails"


EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

if env("ENVIRONMENT") == "ci":
    STATIC_URL = "/staticfiles/"
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    MEDIA_URL = "/media/"

else:
    USE_S3 = env("USE_S3")

    if USE_S3:
        """AWS settings"""
        AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
        AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
        AWS_DEFAULT_ACL = None
        AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
        AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

        """S3 static settings"""
        STATIC_LOCATION = "static"
        STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
        STATICFILES_STORAGE = "core.storage_backends.StaticStorage"

        """s3 media settings"""
        PUBLIC_MEDIA_LOCATION = "media"
        MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
        DEFAULT_FILE_STORAGE = "core.storage_backends.PublicMediaStorage"
    else:
        STATIC_URL = "/staticfiles/"
        STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

        MEDIA_ROOT = os.path.join(BASE_DIR, "media")
        MEDIA_URL = "/media/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
