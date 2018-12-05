from PySide2 import QtWidgets
from PySide2 import QtGui
from ..contacts_model import ContactsModel


class ContactsWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vbox_layout = QtWidgets.QVBoxLayout()
        self.hbox_layout = QtWidgets.QHBoxLayout()
        self.open_contacts = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/folder-open-document.png"), "Otvori", self)
        self.add_button = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/plus.png"), "Dodaj", self)
        self.edit_button = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/pencil.png"), "Izmeni", self)
        self.remove_button = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/minus.png"), "Obrisi", self)
        self.hbox_layout.addWidget(self.open_contacts)
        self.hbox_layout.addWidget(self.add_button)
        self.hbox_layout.addWidget(self.edit_button)
        self.hbox_layout.addWidget(self.remove_button)
        self.table_view = QtWidgets.QTableView(self)

        self.table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        #self.table_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)


        self.open_contacts.clicked.connect(self._on_open)
        self.remove_button.clicked.connect(self._on_remove)

        self.vbox_layout.addLayout(self.hbox_layout)
        self.vbox_layout.addWidget(self.table_view)

        self.setLayout(self.vbox_layout)

        self.actions_dict = {
            "add": QtWidgets.QAction(QtGui.QIcon("resources/icons/plus.png"), "Dodaj", self)
        }


    def set_model(self, model):
        self.table_view.setModel(model)

    def _on_open(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, "Open contacts file", ".", "CSV Files (*.csv)")
        self.table_view.setModel(ContactsModel(path[0]))

    def _on_add(self):
        pass

    def _on_edit(self):
        pass

    def _on_remove(self):
        self.table_view.model().remove(self.table_view.selectedIndexes())
