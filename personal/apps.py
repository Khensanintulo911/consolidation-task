from django.apps import AppConfig


class PersonalConfig(AppConfig):
    """
    Configuration class for the 'personal' Django application.

    Attributes:
        default_auto_field (str): Specifies the type of auto-created primary key field.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal'
