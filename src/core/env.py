from environ import Env
from django.core.management.utils import get_random_secret_key

env = Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, get_random_secret_key()),
    EMAIL_HOST_USER=(str, "apikey"),
    EMAIL_HOST_PASSWORD=(
        str,
        None,
    ),
    DEFAULT_FROM_EMAIL=(str, None),
    USE_S3=(bool, False),
    USE_RDS=(bool, False),
    DB_USER=(str, "db_warehouse"),
    DB_PASSWORD=(str, "db_warehouse"),
    DB_NAME=(str, "db_warehouse"),
    DB_HOST=(str, "db"),
)
