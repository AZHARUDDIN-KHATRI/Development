import time
import psutil


def track_system_resources(interval=1.0):
    """Continuously tracks and prints CPU and memory usage."""
    print("Starting CPU and Memory Tracker. Press Ctrl+C to stop.\n")
    try:
        while True:
            # Get CPU usage percentage over the given interval
            cpu_usage = psutil.cpu_percent(interval=None)
            
            # Get virtual memory statistics
            mem = psutil.virtual_memory()
            mem_total_gb = mem.total / (1024 ** 3)
            mem_used_gb = mem.used / (1024 ** 3)
            mem_percent = mem.percent
            
            # Print metrics
            print(f"CPU Usage: {cpu_usage:5.1f}% | "
                  f"RAM Used: {mem_used_gb:4.2f} GB / {mem_total_gb:4.2f} GB ({mem_percent:5.1f}%)",
                  end="\r")
            
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    track_system_resources(interval=1.0)