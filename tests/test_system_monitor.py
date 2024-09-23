import unittest
from core.system_monitor import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = SystemMonitor()

    def test_get_cpu_usage(self):
        cpu_usage = self.monitor.get_cpu_usage()
        self.assertIsInstance(cpu_usage, float, "CPU Usage should be a float")
        self.assertGreaterEqual(cpu_usage, 0, "CPU Usage should be greater than or equal to 0")

    def test_get_ram_usage(self):
        ram_usage = self.monitor.get_ram_usage()
        self.assertIsInstance(ram_usage, float, "RAM Usage should be a float")
        self.assertGreaterEqual(ram_usage, 0, "RAM Usage should be greater than or equal to 0")

    def test_get_cpu_temperature(self):
        temp = self.monitor.get_cpu_temperature()
        if temp is not None:
            self.assertIsInstance(temp, float, "CPU Temperature should be a float")

    def test_get_fan_speed(self):
        fan_speed = self.monitor.get_fan_speed()
        if fan_speed is not None:
            self.assertIsInstance(fan_speed, int, "Fan speed should be an integer")

if __name__ == '__main__':
    unittest.main()
