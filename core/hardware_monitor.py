# core/hardware_monitor.py

import psutil

class HardwareMonitor:
    def get_disk_usage(self):
        """Returns the disk usage percentage of the root partition."""
        return psutil.disk_usage('/').percent
