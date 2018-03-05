# encoding:utf-8
import importlib

from plugboard.exceptions import SettingsImportError
from .global_settings import GlobalSettings


class ConfigSettings(dict):
    """
    """
    def __init__(self, defaults=GlobalSettings):
        super(dict, self).__init__()
        self.defaults = defaults
        self.setup()

    def setup(self):
        """
        load settings form default global
        :return:
        """
        self.from_object(self.defaults)

    def import_string(self, path, silent):
        """
        :param path:
        :param silent:
        :return:
        """
        import_name = path.replace(":", ".")
        module_path, cls_obj = import_name.rsplit(".", 1)
        try:
            module = importlib.import_module(module_path)
            if hasattr(module, cls_obj):
                return getattr(module, cls_obj)
            else:
                if not silent:
                    raise SettingsImportError("import <%s>.<%s> class does not exist" % (module_path, cls_obj))

        except (ImportError, AttributeError):
            if not silent:
                raise SettingsImportError("<%s>Settings Import Error" % path)

    def from_object(self, obj, silent=True):
        """
        # local settings from pyobject
        if obj -> str,
         from_object("app.config")
        :param obj:
        :param silent:
        :return:
        """
        if isinstance(obj, str):
            obj = self.import_string(obj, silent)
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, dict.__repr__(self))


config = ConfigSettings()
