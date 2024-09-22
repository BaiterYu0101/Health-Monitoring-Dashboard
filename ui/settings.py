# ui/settings.py

from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QVBoxLayout

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Settings')
        self.init_ui()

    def init_ui(self):
        # Theme selection
        theme_label = QLabel('Select Theme:')
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(['Light', 'Dark'])

        # Save button
        save_button = QPushButton('Save')
        save_button.clicked.connect(self.save_settings)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(theme_label)
        layout.addWidget(self.theme_combo)
        layout.addWidget(save_button)
        self.setLayout(layout)

    def save_settings(self):
        selected_theme = self.theme_combo.currentText()
        # Here you can implement saving the theme to a config file or apply it
        print(f'Theme selected: {selected_theme}')
        self.close()
