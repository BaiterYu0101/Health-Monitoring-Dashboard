# core/notifications.py

from PyQt5.QtWidgets import QMessageBox

class NotificationHandler:
    def show_warning(self, title, message):
        """Displays a warning message box."""
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()
