# core/notifications.py

from PyQt5.QtWidgets import QMessageBox, QApplication, QPushButton

class NotificationHandler:
    def show_warning(self, title, message):
        """Displays a warning message box."""
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # Add optimize and cancel button
        optimize_button = QPushButton("Optimize")
        stop_button = QPushButton("Stop showing error message")

        # Add the button to message box
        msg_box.addButton(optimize_button, QMessageBox.AcceptRole)
        msg_box.addButton(stop_button, QMessageBox.AcceptRole)

        # Capture the user's response
        response = msg_box.exec_()


