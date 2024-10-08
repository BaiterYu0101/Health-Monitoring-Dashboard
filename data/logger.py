import logging
import csv
import os
from datetime import datetime

class Logger:
    def __init__(self):
        # Configure logging
        logging.basicConfig(
            filename='data/system_health.log',
            level=logging.INFO,
            format='%(asctime)s:%(levelname)s:%(message)s'
        )
        # Ensure performance data file exists
        self.performance_data_file = 'data/performance_data.csv'
        if not os.path.isfile(self.performance_data_file):
            with open(self.performance_data_file, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['timestamp', 'cpu_usage', 'ram_usage', 'disk_usage', 'cpu_temp', 'fan_speed'])

    def log_info(self, message):
        logging.info(message)

    def log_warning(self, message):
        logging.warning(message)

    def log_error(self, message):
        logging.error(message)

    def log_performance_data(self, cpu_usage, ram_usage, disk_usage, cpu_temp=None, fan_speed=None):
        """Logs performance data to CSV."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.performance_data_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([timestamp, cpu_usage, ram_usage, disk_usage, cpu_temp, fan_speed])

        # Also log the data to the system_health.log file
        log_message = (
            f"Timestamp: {timestamp}, CPU Usage: {cpu_usage}%, RAM Usage: {ram_usage}%, "
            f"Disk Usage: {disk_usage}%, CPU Temperature: {cpu_temp} °C, Fan Speed: {fan_speed} RPM"
        )
        self.log_info(log_message)
