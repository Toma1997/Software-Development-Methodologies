from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt

class PluginDialog(QtWidgets.QDialog):
    def __init__(self, title="Plugin settings", parent=None, plugin_service=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.resize(600, 400)

        self.plugin_service = plugin_service

        self.plugin_options_layout = QtWidgets.QHBoxLayout()

        self.set_button = QtWidgets.QPushButton(QIcon("resources/icons/application-plus.png"), "Set as central")
        self.uninstall_button = QtWidgets.QPushButton(QIcon("resources/icons/minus-circle.png"), "Uninstall")
        self.enable_button = QtWidgets.QPushButton(QIcon("resources/icons/tick.png"), "Enable")
        self.disable_button = QtWidgets.QPushButton(QIcon("resources/icons/minus.png"), "Disable")
        self.plugin_dialog_layout = QtWidgets.QVBoxLayout()

        self.plugins_table = QtWidgets.QTableWidget(self)

        self.plugin_options_layout.addWidget(self.set_button)
        self.plugin_options_layout.addWidget(self.uninstall_button)
        self.plugin_options_layout.addWidget(self.enable_button)
        self.plugin_options_layout.addWidget(self.disable_button)

        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.on_accept)
        self.button_box.rejected.connect(self.on_reject)

        self.set_button.pressed.connect(self.on_set)

        self._populate_table()

        self.plugin_dialog_layout.addLayout(self.plugin_options_layout)
        self.plugin_dialog_layout.addWidget(self.plugins_table)
        self.plugin_dialog_layout.addWidget(self.button_box)

        self.setLayout(self.plugin_dialog_layout)

    def on_set(self):
        # FIXME: dobavi selekciju i aktiviraj widget
        self.parent().set_central_widget(self.parent().plugin_service.get_by_symbolic_name("rs.ac.singidunum.imenik").get_widget())

    def on_accept(self):
        return self.accept()

    def on_reject(self):
        return self.reject()

    def _populate_table(self):
        self.plugins_table.setColumnCount(5)
        self.plugins_table.setHorizontalHeaderLabels(
            ["Name", "Version", "Description", "Symbolic name", "Enabled"])
        # TODO: list all plugins
        self.plugins_table.setRowCount(len(self.plugin_service.plugins))
        for i, plugin in enumerate(self.plugin_service.plugins):
            name = QtWidgets.QTableWidgetItem(plugin.name)
            version = QtWidgets.QTableWidgetItem(plugin.version)
            description = QtWidgets.QTableWidgetItem(plugin.description)
            symbolic_name = QtWidgets.QTableWidgetItem(plugin.symbolic_name)
            enabled = QtWidgets.QTableWidgetItem("Enabled" if plugin.enabled else "Disabled")

            name.setFlags(name.flags() ^ Qt.ItemIsEditable)
            version.setFlags(version.flags() ^ Qt.ItemIsEditable)
            description.setFlags(description.flags() ^ Qt.ItemIsEditable)
            symbolic_name.setFlags(symbolic_name.flags() ^ Qt.ItemIsEditable)

            self.plugins_table.setItem(i, 0, name)
            self.plugins_table.setItem(i, 1, version)
            self.plugins_table.setItem(i, 2, description)
            self.plugins_table.setItem(i, 3, symbolic_name)
            self.plugins_table.setItem(i, 4, enabled)


