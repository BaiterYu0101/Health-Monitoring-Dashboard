import psutil

class SystemMonitor:
    def get_cpu_usage(self):
        """Returns the current CPU usage percentage."""
        return psutil.cpu_percent(interval=1)

    def get_ram_usage(self):
        """Returns the current RAM usage percentage."""
        return psutil.virtual_memory().percent

    def get_cpu_temperature(self):
        """Returns the current CPU temperature in degrees Celsius."""
        temperatures = psutil.sensors_temperatures()
        for name, entries in temperatures.items():
            for entry in entries:
                if name.lower() == 'coretemp':  # Typically 'coretemp' for CPUs
                    return entry.current
        return None

    def get_fan_speed(self):
        """Returns the current fan speed in RPM."""
        fans = psutil.sensors_fans()
        if fans:
            for name, entries in fans.items():
                for entry in entries:
                    return entry.current  # Returns the first fan speed detected
        return None
