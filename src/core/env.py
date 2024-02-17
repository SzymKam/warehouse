from environ import Env
from django.core.management.utils import get_random_secret_key

env = Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, get_random_secret_key()),
    EMAIL_HOST_USER=(str, "apikey"),
    EMAIL_HOST_PASSWORD=(
        str,
        None,
    ),
    DEFAULT_FROM_EMAIL=(str, None),
    TEST_PASSWORD=(str, None),
    USE_S3=(bool, False),
    USE_RDS=(bool, False),
    ENVIRONMENT=(str, None),
    USER=(str, "db_warehouse"),
    PASSWORD=(str, "db_warehouse"),
    NAME=(str, "db_warehouse"),
    HOST=(str, "db"),
)
