# tests/test_system_monitor.py

import unittest
from core.system_monitor import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = SystemMonitor()

    def test_get_cpu_usage(self):
        cpu_usage = self.monitor.get_cpu_usage()
        self.assertIsInstance(cpu_usage, float)
        self.assertGreaterEqual(cpu_usage, 0)
        self.assertLessEqual(cpu_usage, 100)

    def test_get_ram_usage(self):
        ram_usage = self.monitor.get_ram_usage()
        self.assertIsInstance(ram_usage, float)
        self.assertGreaterEqual(ram_usage, 0)
        self.assertLessEqual(ram_usage, 100)

if __name__ == '__main__':
    unittest.main()
