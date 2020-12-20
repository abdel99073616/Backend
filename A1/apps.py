from django.apps import AppConfig


class A1Config(AppConfig):
    name = 'A1'


    def ready(self):
        import A1.signals
