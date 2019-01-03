from plugin_framework.plugin import Plugin

class Main(Plugin):
    """
    Primer prvog plugina.
    """
    def __init__(self, spec):
        super().__init__(spec)

    def hello(self):
        print("Hello world (first)!")
