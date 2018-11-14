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