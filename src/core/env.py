import environ
from django.core.management.utils import get_random_secret_key

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, get_random_secret_key()),
    USER=(str, "db_warehouse"),
    PASSWORD=(str, "db_warehouse"),
    NAME=(str, "db_warehouse"),
    HOST=(str, "db"),
    EMAIL_HOST_USER=(str, "apikey"),
    EMAIL_HOST_PASSWORD=(
        str,
        None,
    ),
    DEFAULT_FROM_EMAIL=(str, None),
    TEST_PASSWORD=(str, None),
)
