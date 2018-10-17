from plugin_framework.plugin import Plugin

class ConcretePlugin(Plugin):
    def __init__(self, name, size, category, version, enabled, description):
        super().__init__(name, size, category, version, enabled, description)

    def hello(self):
        print("Hello world!")
