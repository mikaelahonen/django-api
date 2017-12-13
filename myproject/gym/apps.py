#https://stackoverflow.com/questions/7115097/the-right-place-to-keep-my-signals-py-files-in-django
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'gym'

    def ready(self):
        import gym.signals
