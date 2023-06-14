import environ
from django.core.management.utils import get_random_secret_key

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, get_random_secret_key()),
    USER=(str, "user"),
    PASSWORD=(str, "user"),
    EMAIL_HOST_USER=(str, "apikey"),
    EMAIL_HOST_PASSWORD=(
        str,
        "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",
    ),
    DEFAULT_FROM_EMAIL=(str, "szymon15kaminski@gmail.com"),
)
