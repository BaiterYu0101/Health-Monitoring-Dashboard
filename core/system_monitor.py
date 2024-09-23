import os
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
        if os.name == 'posix':  # Linux/Unix
            return self.get_cpu_temperature_linux()
        elif os.name == 'nt':  # Windows
            return self.get_cpu_temperature_windows()
        return None

    def get_cpu_temperature_linux(self):
        temperatures = psutil.sensors_temperatures()
        for name, entries in temperatures.items():
            for entry in entries:
                if name.lower() == 'coretemp':  # Typically 'coretemp' for CPUs
                    return entry.current
        return None

    def get_cpu_temperature_windows(self):
        try:
            import wmi
            w = wmi.WMI(namespace="root\wmi")
            temperature_infos = w.MSAcpi_ThermalZoneTemperature()
            for info in temperature_infos:
                return (info.CurrentTemperature / 10.0) - 273.15  # Convert from tenths of Kelvin to Celsius
        except ImportError:
            print("WMI module not installed, please install it to fetch temperatures on Windows.")
        except Exception as e:
            print(f"Failed to read temperature: {str(e)}")
        return None

    def get_fan_speed(self):
        """Returns the current fan speed in RPM."""
        fans = psutil.sensors_fans()
        if fans:
            for name, entries in fans.items():
                for entry in entries:
                    return entry.current  # Returns the first fan speed detected
        return None
