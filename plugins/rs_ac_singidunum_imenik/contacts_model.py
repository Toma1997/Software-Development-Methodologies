from PySide2 import QtCore
import csv
import os


class ContactsModel(QtCore.QAbstractTableModel):
    def __init__(self, path=""):
        super().__init__()
        self._data = []
        self.load_data(path)

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return 5

    def data(self, index, role):
        element = self.get_element(index)
        if element is None:
            return None

        if role == QtCore.Qt.DisplayRole:
            return element
    
    def headerData(self, section, orientation, role):
        if orientation != QtCore.Qt.Vertical:
            if (section == 0) and (role == QtCore.Qt.DisplayRole):
                return "Ime"
            elif (section == 1) and (role == QtCore.Qt.DisplayRole):
                return "Prezime"
            elif (section == 2) and (role == QtCore.Qt.DisplayRole):
                return "Email"
            elif (section == 3) and (role == QtCore.Qt.DisplayRole):
                return "Telefon"
            elif (section == 4) and (role == QtCore.Qt.DisplayRole):
                return "Datum rodjenja"

    def setData(self, index, value, role):
        try:
            if value == "":
                return False
            self._data[index.row()][index.column()] = value
            self.dataChanged()
            return True
        except:
            return False

    def flags(self, index):
        if index.column() != 4: # ne damo da menja datum rodjenja (primera radi)
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        else: # sve ostale podatke korisnik moze da menja
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def get_element(self, index : QtCore.QModelIndex):
        if index.isValid():
            element = self._data[index.row()][index.column()]
            if element:
                return element
        return None

    def remove(self, indices):
        indices = sorted(set(map(lambda x: x.row(), indices)), reverse=True)
        for i in indices:
            self.beginRemoveRows(QtCore.QModelIndex(), i, i)
            del self._data[i]
            self.endRemoveRows()

    def add(self, data : dict):
        self.beginInsertRows(QtCore.QModelIndex(), len(self._data), len(self._data))
        self._data.append([data["name"], data["surname"], data["phone"], data["email"], data["birthday"]])
        self.endInsertRows()

    def load_data(self, path=""):
        with open(path, "r", encoding="utf-8") as fp:
            self._data = list(csv.reader(fp))


