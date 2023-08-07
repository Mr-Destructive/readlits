from .settings import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),  # noqa
        "HOST": env("DB_HOST"),  # noqa
        "USER": env("DB_USER"),  # noqa
        "PASSWORD": env("DB_PASSWORD"),  # noqa
        "PORT": env("DB_PORT"),  # noqa
    }
}
