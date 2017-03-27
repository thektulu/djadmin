# ACTION_CHECKBOX_NAME is unused, but should stay since its import from here
# has been referenced in documentation.
from djadmin.decorators import register
from djadmin.filters import (
    AllValuesFieldListFilter, BooleanFieldListFilter, ChoicesFieldListFilter,
    DateFieldListFilter, FieldListFilter, ListFilter, RelatedFieldListFilter,
    RelatedOnlyFieldListFilter, SimpleListFilter,
)
from djadmin.helpers import ACTION_CHECKBOX_NAME
from djadmin.options import (
    HORIZONTAL, VERTICAL, ModelAdmin, StackedInline, TabularInline,
)
from djadmin.sites import AdminSite, site
from djadmin.monkey_patch import apply_monkeypatches

from django.utils.module_loading import autodiscover_modules
from django.utils.version import get_version

__all__ = [
    "register", "ACTION_CHECKBOX_NAME", "ModelAdmin", "HORIZONTAL", "VERTICAL",
    "StackedInline", "TabularInline", "AdminSite", "site", "ListFilter",
    "SimpleListFilter", "FieldListFilter", "BooleanFieldListFilter",
    "RelatedFieldListFilter", "ChoicesFieldListFilter", "DateFieldListFilter",
    "AllValuesFieldListFilter", "RelatedOnlyFieldListFilter", "autodiscover",
]


def autodiscover():
    autodiscover_modules('djadmin', register_to=site)


def monkeypathes():
    apply_monkeypatches()


VERSION = (0, 11, 0, 'alpha', 0)

__version__ = get_version(version=VERSION)

default_app_config = 'djadmin.apps.AdminConfig'
