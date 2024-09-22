<h1>System Health Dashboard</h1>    
<p>A cross-platform desktop application to monitor system health metrics such as CPU usage, RAM usage, disk space, and more. Built with Python and PyQt5, it provides real-time monitoring, notifications, and optimization suggestions to keep your system running smoothly.</p><br>

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Usage](#usage)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Additional Resourrces](#additionalresources)


## Features
<ul>
  <li>Real-time Monitoring: Displays CPU, RAM, and Disk usage in real-time.</li>
  <li>Notifications: Alerts for high resource usage with optimization suggestions.</li>
  <li>Optimization Advice: Provides tips to improve system performance.</li>
  <li>Settings: Customize application settings like themes.</li>
  <li>Data Logging: Logs historical performance data for analysis.</li>
  <li>Cross-Platform: Works on Windows, macOS, and Linux.</li>
  <li>Extensible: Modular code structure for easy enhancements.</li>
  <li>Unit Tests: Comprehensive tests for core functionalities.</li>
</ul>


## Screenshots
  Wait for deployment and snap


## Installation

  ### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

  ### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/system-health-dashboard.git
   cd system-health-dashboard

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv

3. **Activate the Virtual Environment**

- On **Windows**:

   ```bash
   venv\Scripts\activate
   ```
   
- On **Linux**:

  ```bash
  source venv/bin/activate
  ```
  
4. **Install Dependencies**
  ```bash
  pip install -r requirements.txt
  ```
## Usage

1. **Run the Application**
  ```bash
  python main.py
  ```

2. **Navigate the Dashboard**
  - **CPU Usage**: Monitor your CPU usage in real-time.
  - **RAM Usage**: Keep an eye on your memory consumption.
  - **Disk Usage**: Check available disk space.
  - **Optimization Advice**: Get tips to enhance performance.
  - **Settings**: Customize the application to your preferences.

3. **Received Notification**
  - Alerts will pop up if CPU or RAM usage exceeds 90%.
  - Follow the optimization advice to mitigate high resource usage.



## Configuration

  ### Settngs
  - **Themes**: Switch between Light and Dark modes.
  - **Notification Thresholds**: (Future enhancement) Set custom thresholds for alerts.

  ### How to Access Settings
  - Click on the "**Settings**" button on the dashboard to open the settings window.
  - Adjust your preferences and click "**Save**".

## Running Tests
1. **Activate the Virtual Environment**
    Ensure VE is active:
   ```bash
   # On Windows
   venv\Scripts\activate

   # On Linux
   sourrce venv/bin/activate
   ```
2. **Run Test**
   ```bash
   python -m unittest discover tests
   ```

## Project Structure

```bash
system-health-dashboard/
│
├── venv/                       # Virtual environment directory
│
├── main.py                     # Entry point for the application
│
├── core/                       # Core functionalities
│   ├── __init__.py
│   ├── system_monitor.py       # System monitoring logic (CPU, RAM)
│   ├── notifications.py        # Notification handling
│   ├── hardware_monitor.py     # Hardware-specific metrics (disk)
│   └── optimization.py         # System optimization suggestions
│
├── ui/                         # User interface files
│   ├── __init__.py
│   ├── dashboard.py            # Main GUI code
│   ├── settings.py             # Settings window
│   └── styles.css              # CSS styles for the UI
│
├── data/                       # Data handling and logging
│   ├── __init__.py
│   ├── logger.py               # Logging system operations
│   ├── performance_data.csv    # Historical performance data
│   ├── disk_usage_report.txt   # Disk usage report
│   └── hardware_diagnostics.txt# Hardware diagnostics
│
├── models/                     # Machine learning models
│   ├── __init__.py
│   └── predictive_maintenance.py# Predictive maintenance logic
│
├── resources/                  # Static resources (images, logos)
│   ├── logo.png
│   ├── dashboard_view.png
│   └── settings_window.png
│
├── tests/                      # Unit tests
│   ├── __init__.py
│   ├── test_system_monitor.py  # Tests for system monitoring
│   └── test_hardware_monitor.py# Tests for hardware monitoring
│
├── README.md                   # Project documentation
└── requirements.txt            # Dependencies
```

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- **PyQt5**: For the cross-platform GUI toolkit.
- **psutil**: For accessing system health metrics.
- **Matplotlib**: For potential future enhancements with data visualization.
- **Open-Source Community**: For providing valuable resources and inspiration.

## Additional Resources

- **PyQt5 Documentation**: [https://www.riverbankcomputing.com/static/Docs/PyQt5/](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- **psutil Documentation**: [https://psutil.readthedocs.io/en/latest/](https://psutil.readthedocs.io/en/latest/)
- **Python Virtual Environments**: [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html)
