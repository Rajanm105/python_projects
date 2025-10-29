import psutil
import time
import os

def get_sys_info():
    cpu_per = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('C:\\')
    network_info = psutil.net_io_counters()

    return {
            "cpu_percent": cpu_per,
            "memory_total": memory.total,
            "memory_used": memory.used,
            "memory_percent": memory.percent,
            "disk_total": disk_usage.total,
            "disk_used": disk_usage.used,
            "disk_percent": disk_usage.percent,
            "net_bytes_sent": network_info.bytes_sent,
            "net_bytes_recv": network_info.bytes_recv,
        }

def monitor_system():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear') # Clear screen
            stats = get_sys_info()

            print("--- System Monitor ---")
            print(f"CPU Usage: {stats['cpu_percent']}%")
            print(f"Memory Usage: {stats['memory_percent']}% ({stats['memory_used'] / (1024**3):.2f}GB / {stats['memory_total'] / (1024**3):.2f}GB)")
            print(f"Disk Usage: {stats['disk_percent']}% ({stats['disk_used'] / (1024**3):.2f}GB / {stats['disk_total'] / (1024**3):.2f}GB)")
            print(f"Network (Sent/Received): {stats['net_bytes_sent'] / (1024**2):.2f}MB / {stats['net_bytes_recv'] / (1024**2):.2f}MB")

            time.sleep(2) # Update every 2 seconds

if __name__ == "__main__":
    monitor_system()