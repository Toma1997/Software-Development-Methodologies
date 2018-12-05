from plugin_framework.plugin_service import PluginService


import sys
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from gui.main_window import MainWindow
                                                     
if __name__ == "__main__":
    plugin_service = PluginService()
    plugin_service.load_plugins()

    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow(plugin_service)
    main_window.show()
    sys.exit(app.exec_())