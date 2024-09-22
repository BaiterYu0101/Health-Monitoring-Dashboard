# core/optimization.py

class OptimizationAdvisor:
    def get_cpu_advice(self, cpu_usage):
        if cpu_usage > 80:
            return "High CPU usage detected. Close unnecessary applications."
        return "CPU usage is normal."

    def get_ram_advice(self, ram_usage):
        if ram_usage > 80:
            return "High RAM usage detected. Consider closing some programs."
        return "RAM usage is normal."
