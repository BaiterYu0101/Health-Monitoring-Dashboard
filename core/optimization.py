# core/optimization.py

class OptimizationAdvisor:
    
    def get_cpu_ram_advice(self, cpu_usage, ram_usage,disk_usage):
        match(cpu_usage, ram_usage,disk_usage):
            case(cpu, _, _) if cpu > 5:
                return "High CPU usage detected. Close unnecessary applications."
            case(_,ram, _) if ram > 90:
                return "High RAM usage detected. Consider closing some programs."
            case( _, _,disk) if disk > 90:
                return "The disk is running low on available storage."
            case  _:
                return "All are normal"