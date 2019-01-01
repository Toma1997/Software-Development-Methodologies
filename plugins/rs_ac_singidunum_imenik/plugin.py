from plugin_framework.plugin import Plugin
from .widgets.contacts_widget import ContactsWidget

class Main(Plugin):
    """
    Klasa koja predstavlja konkretni plugin. Nasledjujemo "apstraktnu" klasu Plugin.
    Ova klasa predstavlja plugin za aplikaciju kontakti (imenik).
    """
    def __init__(self, spec):
        """
        Inicijalizator imenik plugina.

        :param spec: specifikacija metapodataka o pluginu.
        :type spec: dict
        """
        super().__init__(spec)

    def get_widget(self, parent=None):
        """
        Ova metoda vraca konkretni widget koji ce biti smesten u centralni deo aplikacije i njenog 
        glavnog prozora.

        :param spec: specifikacija metapodataka o pluginu.
        :type spec: dict
        :returns: ContactWidget
        """
        # TODO: Dodati da svaki plugin ima ovu metodu. Ova metoda bi trebala da vraca svoj meni i svoj toolbar
        # FIXME: Uraditi u sledecoj verziji (u XV nedelji nastave)
        return ContactsWidget(parent)