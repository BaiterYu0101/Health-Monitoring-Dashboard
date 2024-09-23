# ui/dashboard.py

from PyQt5.QtWidgets import (
    QMainWindow, QLabel, QProgressBar, QVBoxLayout, QWidget, QPushButton
)
from PyQt5.QtCore import QTimer
from core.system_monitor import SystemMonitor
from core.hardware_monitor import HardwareMonitor
from core.optimization import OptimizationAdvisor
from core.notifications import NotificationHandler
from ui.settings import SettingsWindow
from data.logger import Logger

class DashboardApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('System Health Dashboard')

        # Initialize components
        self.system_monitor = SystemMonitor()
        self.hardware_monitor = HardwareMonitor()
        self.optimization_advisor = OptimizationAdvisor()
        self.notification_handler = NotificationHandler()
        self.logger = Logger()

        # Setup UI
        self.init_ui()

        # Start timers
        self.init_timers()

    def init_ui(self):
        # Labels and progress bars
        self.cpu_label = QLabel('CPU Usage:')
        self.cpu_progress = QProgressBar()
        self.cpu_progress.setRange(0, 100)

        self.ram_label = QLabel('RAM Usage:')
        self.ram_progress = QProgressBar()
        self.ram_progress.setRange(0, 100)

        self.disk_label = QLabel('Disk Usage:')
        self.disk_progress = QProgressBar()
        self.disk_progress.setRange(0, 100)

        self.advice_label = QLabel('Advice:')

        # Settings button
        self.settings_button = QPushButton('Settings')
        self.settings_button.clicked.connect(self.open_settings)

        # Layouts
        layout = QVBoxLayout()
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.cpu_progress)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.ram_progress)
        layout.addWidget(self.disk_label)
        layout.addWidget(self.disk_progress)
        layout.addWidget(self.advice_label)
        layout.addWidget(self.settings_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def init_timers(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)  # Update every second

    def update_metrics(self):
        cpu_usage = self.system_monitor.get_cpu_usage()
        ram_usage = self.system_monitor.get_ram_usage()
        disk_usage = self.hardware_monitor.get_disk_usage()

        # Convert usage values to integers
        cpu_usage_int = int(cpu_usage)
        ram_usage_int = int(ram_usage)
        disk_usage_int = int(disk_usage)  # Corrected variable name

        # Update progress bars
        self.cpu_progress.setValue(cpu_usage_int)
        self.ram_progress.setValue(ram_usage_int)
        self.disk_progress.setValue(disk_usage_int)

        # Update labels with precise values
        self.cpu_label.setText(f'CPU Usage: {cpu_usage:.2f}%')
        self.ram_label.setText(f'RAM Usage: {ram_usage:.2f}%')
        self.disk_label.setText(f'Disk Usage: {disk_usage:.2f}%')

        advice = self.optimization_advisor.get_cpu_ram_advice(cpu_usage,ram_usage,disk_usage)
        self.advice_label.setText(f'Advice: {advice}')

        # Log data
        self.logger.log_performance_data(cpu_usage, ram_usage, disk_usage)

        # Show warning message box
        if cpu_usage > 5 or ram_usage > 90 or disk_usage > 90:
            self.notification_handler.show_warning("Warning", advice)

    def open_settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()
