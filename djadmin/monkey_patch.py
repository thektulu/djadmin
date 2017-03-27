
__patches__ = [
    'django_db_models_options',
]


def apply_monkeypatches():
    _globals = globals()
    for patch_name in __patches__:
        _globals[patch_name]()


def django_db_models_options():
    from django.db.models.options import Options
    orig_init = Options.__init__
    def __init__(self, meta, app_label=None):
        orig_init(self, meta, app_label)
        self.default_permissions = self.default_permissions + ('view', )

    Options.__init__ = __init__
