from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username=os.environ['ADMIN_USER']).exists():
            User.objects.create_superuser(os.environ['ADMIN_USER'], os.environ['ADMIN_EMAIL'], os.environ['ADMIN_PASS'])