from django.apps import AppConfig


class CoreConfig(AppConfig):
    # It's an auto-incrementing field that automatically generates unique IDs for each new record
    # uses a 64-bit integer to store the ID -> future-proofing application so won't run out of IDs
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
