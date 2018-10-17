from student import Student
from person import Person
from plugins.concrete_plugin import ConcretePlugin
from plugin_framework.plugin_service import PluginService

"""
o = Person("Aleksandra", "Mitrovic")
print(o.name)
o.name = "Janko"
print(o.name)

s = Student("Marko", "Markovic", "Rgjk1132")
print(s.name)
"""


plugin_service = PluginService()
plugin1 = ConcretePlugin("Naziv", 10, "opsta", "1.0.0", True, "Kratki opis plugina.")
plugin_service.install(plugin1)
plugin1.hello()