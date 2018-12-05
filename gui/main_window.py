from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from gui.dialogs.plugin_dialog import PluginDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ps, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Univerzitet Singidunum")
        self.resize(800, 600)
        self.setWindowIcon(QIcon("resources/icons/abacus.png"))

        self.plugin_service = ps

        self.action_dict = {
            "open":  QtWidgets.QAction(QIcon("resources/icons/folder-open-document.png"), "&Open document"),
            "plugin_settings": QtWidgets.QAction(QIcon("resources/icons/puzzle.png"), "&Plugin settings")
        }

        self.menu_bar = QtWidgets.QMenuBar(self)
        self.tool_bar = QtWidgets.QToolBar("Toolbar", self)

        self.file_menu = QtWidgets.QMenu("&File", self.menu_bar)
        self.view_menu = QtWidgets.QMenu("&View", self.menu_bar)
        self.tools_menu = QtWidgets.QMenu("&Tools", self.menu_bar)
        self.help_menu = QtWidgets.QMenu("&Help", self.menu_bar)

        self.central_widget = QtWidgets.QTextEdit(self)

        self._bind_actions()
        self._populate_menu_bar()
        self._populate_tool_bar()

        self.setCentralWidget(self.central_widget)
        self.addToolBar(self.tool_bar)
        self.setMenuBar(self.menu_bar)

    def _populate_menu_bar(self):
        self.file_menu.addAction(self.action_dict["open"])
        self.view_menu.addAction(self.tool_bar.toggleViewAction())
        self.tools_menu.addAction(self.action_dict["plugin_settings"])
        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.view_menu)
        self.menu_bar.addMenu(self.tools_menu)
        self.menu_bar.addMenu(self.help_menu)

    def _populate_tool_bar(self):
        self.tool_bar.addAction(self.action_dict["open"])

    def _bind_actions(self):
        self.action_dict["open"].triggered.connect(self.on_open)
        self.action_dict["plugin_settings"].triggered.connect(self.on_open_plugin_settings_dialog)

    def on_open(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Open python file", ".", "Python Files (*.py)")
        with open(file_name[0], "r") as fp:
            text_from_file = fp.read()
            self.central_widget.setText(text_from_file)

    def on_open_plugin_settings_dialog(self):
        dialog = PluginDialog("Plugin settings", self, self.plugin_service)
        dialog.exec_()

    def set_central_widget(self, widget):
        self.setCentralWidget(widget)

