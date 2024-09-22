# core/system_monitor.py

import psutil

class SystemMonitor:
    def get_cpu_usage(self):
        """Returns the current CPU usage percentage."""
        return psutil.cpu_percent(interval=1)

    def get_ram_usage(self):
        """Returns the current RAM usage percentage."""
        return psutil.virtual_memory().percent
