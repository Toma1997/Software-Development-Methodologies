from student import Student
from person import Person
from plugin_framework.plugin_service import PluginService
import json
import os
import importlib

"""
o = Person("Aleksandra", "Mitrovic")
print(o.name)
o.name = "Janko"
print(o.name)

s = Student("Marko", "Markovic", "Rgjk1132")
print(s.name)
"""


plugin_service = PluginService()

def load_plugins(path="plugins"):
    from plugins.rs_ac_singidunum_prvi.plugin import Main as First
    from plugins.rs_ac_singidunum_drugi.plugin import Main as Second
    with open("plugins/rs_ac_singidunum_prvi/spec.json", "r") as fp:
        spec = json.load(fp)
        plugin_service.install(First(spec))
    
    with open("plugins/rs_ac_singidunum_drugi/spec.json", "r") as fp:
        spec = json.load(fp)
        plugin_service.install(Second(spec))

    # for plugin in plugin_service.plugins:
    #     print(plugin.symbolic_name)

load_plugins()
initial_path = "plugins"
for dir in os.listdir(initial_path):
    dir_path = os.path.join(initial_path, dir)
    if os.path.exists(os.path.join(dir_path, "__init__.py")):
        with open(os.path.join(dir_path, "spec.json"), "r") as fp:
            spec = json.load(fp)
            print(os.path.join(dir_path, "plugin"))
            modul = importlib.import_module(os.path.join(dir_path, "plugin").replace(os.sep, "."))
            obj = modul.Main(spec)
            print(obj.symbolic_name)

# from PySide2 import QtWidgets