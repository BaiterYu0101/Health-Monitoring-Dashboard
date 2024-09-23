import sys
import os
from PyQt5.QtWidgets import QApplication
from ui.dashboard import DashboardApp

def main():
    # Display current working directory and Python path for debugging purposes
    print("Current working directory:", os.getcwd())
    print("Python path:", sys.path)

    # Initialize the PyQt5 application
    app = QApplication(sys.argv)

    # Create and display the dashboard application window
    window = DashboardApp()
    window.show()

    # Start the main event loop of the application and exit the script with the status code of the app closure
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
