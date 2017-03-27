"""
Management utility to create superusers.
"""
from __future__ import unicode_literals

from django.apps import apps
from django.contrib.auth.management import create_permissions
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = ('Resync permissions (for "view" default permission'
            ' in existing project)')

    def handle(self, *args, **options):
        for app_config in apps.get_app_configs():
            create_permissions(app_config)
