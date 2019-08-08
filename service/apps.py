from django.apps import AppConfig


class ServiceConfig(AppConfig):
    name = 'service'

    def ready(self):
        import service.signals
