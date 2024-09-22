# tests/test_hardware_monitor.py

import unittest
from core.hardware_monitor import HardwareMonitor

class TestHardwareMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = HardwareMonitor()

    def test_get_disk_usage(self):
        disk_usage = self.monitor.get_disk_usage()
        self.assertIsInstance(disk_usage, float)
        self.assertGreaterEqual(disk_usage, 0)
        self.assertLessEqual(disk_usage, 100)

if __name__ == '__main__':
    unittest.main()
