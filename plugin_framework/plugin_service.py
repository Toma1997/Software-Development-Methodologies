import os
import json
import importlib

class PluginService:
    def __init__(self):
        self._plugins = list()

    def set_enalbled(self, plugin, value):
        if plugin in self._plugins:
            plugin.enabled = value
            return True
        return False

    def install(self, plugin):
        if plugin not in self._plugins:
            self._plugins.append(plugin)
            return True
        return False

    def uninstall(self, plugin):
        if plugin in self._plugins:
            self._plugins.remove(plugin)
            return True
        return False

    @property
    def plugins(self):
        return self._plugins

    def load_plugins(self, plugins_path="plugins"):
        for d in os.listdir(plugins_path):
            dir_path = os.path.join(plugins_path, d)
            if os.path.exists(os.path.join(dir_path, "__init__.py")):
                with open(os.path.join(dir_path, "spec.json"), "r") as fp:
                    spec = json.load(fp)
                    print(os.path.join(dir_path, "plugin"))
                    modul = importlib.import_module(os.path.join(dir_path, "plugin").replace(os.sep, "."))
                    obj = modul.Main(spec)
                    self._plugins.append(obj)