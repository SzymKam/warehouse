import environ
from django.core.management.utils import get_random_secret_key

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, get_random_secret_key()),
    USER=(str, ""),
    PASSWORD=(str, ""),
    HOST=(str, ""),
    EMAIL_HOST_USER=(str, "apikey"),
    EMAIL_HOST_PASSWORD=(
        str,
        None,
    ),
    DEFAULT_FROM_EMAIL=(str, None),
    TEST_PASSWORD=(str, None),
)
