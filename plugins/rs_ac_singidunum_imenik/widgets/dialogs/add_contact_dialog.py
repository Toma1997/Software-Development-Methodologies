from PySide2 import QtWidgets, QtCore

class AddContactDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dodaj kontakt")
        self.vbox_layout = QtWidgets.QVBoxLayout()
        self.form_layout = QtWidgets.QFormLayout()
        self.name_input = QtWidgets.QLineEdit(self)
        self.surname_input = QtWidgets.QLineEdit(self)
        self.email_input = QtWidgets.QLineEdit(self)
        self.birthday_input = QtWidgets.QDateEdit(self)
        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok 
            | QtWidgets.QDialogButtonBox.Cancel, parent=self)

        self.birthday_input.setDate(QtCore.QDate.currentDate())
        self.birthday_input.setCalendarPopup(True)
        self.form_layout.addRow("Ime:", self.name_input)
        self.form_layout.addRow("Prezime:", self.surname_input)
        self.form_layout.addRow("Email:", self.email_input)
        self.form_layout.addRow("Datum rodjenja", self.birthday_input)

        self.vbox_layout.addLayout(self.form_layout)
        self.vbox_layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.setLayout(self.vbox_layout)

    def get_data(self):
        return {
            "name": self.name_input.text(),
            "surname": self.surname_input.text(),
            "email": self.email_input.text(),
            "birthday": self.birthday_input.text()
        }
    



