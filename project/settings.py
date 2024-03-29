from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    ALLOWED_HOSTS=(list, []),
    DEBUG=(bool, False),
    EMAIL_BACKEND=(str, "django.core.mail.backends.console.EmailBackend"),
    ACCOUNT_DEFAULT_HTTP_PROTOCOL=(str, "https"),
)
environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "compressor",
    "readlits.accounts",
    "readlits.books",
    "readlits.core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "project.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Auth

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
AUTH_USER_MODEL = "accounts.User"
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
LOGIN_REDIRECT_URL = "/"


# Emails
EMAIL_BACKEND = env("EMAIL_BACKEND")


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_ROOT = BASE_DIR / "staticfiles" / "static"
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Compressor
COMPRESS_ROOT = BASE_DIR / "static"
COMPRESS_URL = STATIC_URL
COMPRESS_ENABLED = True
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

# SITES
SITE_ID = 1

# django-allauth

# ACCOUNT_ADAPTER => default
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS => default True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL => default
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL => default
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS => default
# ACCOUNT_EMAIL_CONFIRMATION_HMAC => default
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Readlits: "
ACCOUNT_DEFAULT_HTTP_PROTOCOL = env("ACCOUNT_DEFAULT_HTTP_PROTOCOL")
# ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN => default
# ACCOUNT_EMAIL_MAX_LENGTH => default
# ACCOUNT_MAX_EMAIL_ADDRESSES => default
# ACCOUNT_FORMS => default
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT => default
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT => default
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# ACCOUNT_LOGOUT_ON_GET => default
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE => default
# ACCOUNT_LOGIN_ON_PASSWORD_RESET => default
# ACCOUNT_LOGOUT_REDIRECT_URL => default
# ACCOUNT_PASSWORD_INPUT_RENDER_VALUE => default
ACCOUNT_PRESERVE_USERNAME_CASING = False
# ACCOUNT_PREVENT_ENUMERATION => default
# ACCOUNT_RATE_LIMITS => default
ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE => default
# ACCOUNT_SIGNUP_FORM_CLASS => default
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# ACCOUNT_SIGNUP_REDIRECT_URL => default
# ACCOUNT_TEMPLATE_EXTENSION => default
# ACCOUNT_USERNAME_BLACKLIST => default
# ACCOUNT_UNIQUE_EMAIL => default
ACCOUNT_USER_DISPLAY = lambda user: user.email  # noqa
# ACCOUNT_USER_MODEL_EMAIL_FIELD => default
# ACCOUNT_USER_MODEL_USERNAME_FIELD => default
# ACCOUNT_USERNAME_MIN_LENGTH => default
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_USERNAME_VALIDATORS => default
# SOCIALACCOUNT_* => default
