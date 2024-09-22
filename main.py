# main.py

import sys
import os

print("Current working directory:", os.getcwd())
print("Python path:", sys.path)

# from ui.dashboard import DashboardApp


from ui.dashboard import DashboardApp
from PyQt5.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    window = DashboardApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
