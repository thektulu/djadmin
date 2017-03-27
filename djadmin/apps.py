from django.apps import AppConfig
from djadmin.checks import check_admin_app, check_dependencies
from django.core import checks
from django.utils.translation import ugettext_lazy as _


class SimpleAdminConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""

    name = 'djadmin'
    verbose_name = _("Administration")

    def ready(self):
        checks.register(check_dependencies, checks.Tags.admin)
        checks.register(check_admin_app, checks.Tags.admin)


class AdminConfig(SimpleAdminConfig):
    """The default AppConfig for admin which does autodiscovery."""

    def import_models(self, *args):
        self.module.monkeypathes()
        super().import_models(*args)

    def ready(self):
        super(AdminConfig, self).ready()
        self.module.autodiscover()
