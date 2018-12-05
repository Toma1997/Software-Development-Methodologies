from plugin_framework.plugin import Plugin
from .widgets.contacts_widget import ContactsWidget

class Main(Plugin):
    def __init__(self, spec):
        super().__init__(spec)

    def get_widget(self, parent=None):
        return ContactsWidget(parent)