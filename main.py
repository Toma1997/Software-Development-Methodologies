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


# plugin_service = PluginService()

# def load_plugins(path="plugins"):
#     from plugins.rs_ac_singidunum_prvi.plugin import Main as First
#     from plugins.rs_ac_singidunum_drugi.plugin import Main as Second
#     with open("plugins/rs_ac_singidunum_prvi/spec.json", "r") as fp:
#         spec = json.load(fp)
#         plugin_service.install(First(spec))
    
#     with open("plugins/rs_ac_singidunum_drugi/spec.json", "r") as fp:
#         spec = json.load(fp)
#         plugin_service.install(Second(spec))

#     # for plugin in plugin_service.plugins:
#     #     print(plugin.symbolic_name)

# load_plugins()
# initial_path = "plugins"
# for d in os.listdir(initial_path):
#     dir_path = os.path.join(initial_path, d)
#     if os.path.exists(os.path.join(dir_path, "__init__.py")):
#         with open(os.path.join(dir_path, "spec.json"), "r") as fp:
#             spec = json.load(fp)
#             print(os.path.join(dir_path, "plugin"))
#             modul = importlib.import_module(os.path.join(dir_path, "plugin").replace(os.sep, "."))
#             obj = modul.Main(spec)
#             print(obj.symbolic_name)

import sys
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
                                                     
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.setWindowTitle("Univerzitet Singidunum")
    main_window.resize(800, 600)
    main_window.setWindowIcon(QIcon("resources/icons/abacus.png"))

    menu_bar = QtWidgets.QMenuBar(main_window)

    file_menu = QtWidgets.QMenu("&File", menu_bar)
    view_menu = QtWidgets.QMenu("&View", menu_bar)
    help_menu = QtWidgets.QMenu("&Help", menu_bar)

    open_action = QtWidgets.QAction(QIcon("resources/icons/folder-open-document.png"), "&Open document")
    
    file_menu.addAction(open_action)

    menu_bar.addMenu(file_menu)
    menu_bar.addMenu(view_menu)
    menu_bar.addMenu(help_menu)

    toolbar = QtWidgets.QToolBar("Toolbar", main_window)
    toolbar.addAction(open_action)

    view_menu.addAction(toolbar.toggleViewAction())

    central_widget = QtWidgets.QTextEdit(main_window)
    def on_open_document():
        file_name = QtWidgets.QFileDialog.getOpenFileName(main_window, "Open python file", ".", "Python Files (*.py)")
        with open(file_name[0], "r") as fp:
            text_from_file = fp.read()
            central_widget.setText(text_from_file)
    open_action.triggered.connect(on_open_document)
    main_window.setCentralWidget(central_widget)
    main_window.addToolBar(toolbar)
    main_window.setMenuBar(menu_bar)
    main_window.show()
    sys.exit(app.exec_())