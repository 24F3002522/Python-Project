#!/usr/bin/env python3

import os
import platform
import shutil
import time
from datetime import datetime

try:
    import psutil
except ImportError:
    print("Missing dependency: psutil")
    print("Install it using: pip install psutil")
    exit(1)


# ==============================
# Configuration
# ==============================

CPU_LIMIT = 80
RAM_LIMIT = 80
DISK_LIMIT = 85


# ==============================
# Utility Functions
# ==============================

def print_header():
    print("\n" + "=" * 60)
    print("           SERVER HEALTH MONITOR")
    print("=" * 60)
    print(f"Host       : {platform.node()}")
    print(f"OS         : {platform.system()} {platform.release()}")
    print(f"Time       : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


def get_size(bytes_value):
    """Convert bytes into human-readable format."""
    units = ["B", "KB", "MB", "GB", "TB"]

    size = float(bytes_value)

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def check_cpu():
    usage = psutil.cpu_percent(interval=1)

    status = "OK" if usage < CPU_LIMIT else "WARNING"

    print(f"\nCPU Usage     : {usage}%")
    print(f"CPU Status    : {status}")

    return usage


def check_memory():
    memory = psutil.virtual_memory()

    usage = memory.percent

    status = "OK" if usage < RAM_LIMIT else "WARNING"

    print(f"\nRAM Usage     : {usage}%")
    print(f"RAM Used      : {get_size(memory.used)}")
    print(f"RAM Available : {get_size(memory.available)}")
    print(f"RAM Status    : {status}")

    return usage


def check_disk():
    disk = shutil.disk_usage("/")

    usage = (disk.used / disk.total) * 100

    status = "OK" if usage < DISK_LIMIT else "WARNING"

    print(f"\nDisk Usage    : {usage:.2f}%")
    print(f"Disk Used     : {get_size(disk.used)}")
    print(f"Disk Free     : {get_size(disk.free)}")
    print(f"Disk Status   : {status}")

    return usage


def check_uptime():
    boot_time = psutil.boot_time()

    uptime_seconds = time.time() - boot_time

    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)

    print(f"\nSystem Uptime : {days}d {hours}h {minutes}m")


def check_processes():
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent"]
    ):
        try:
            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"] or "Unknown",
                "cpu": info["cpu_percent"] or 0,
                "memory": info["memory_percent"] or 0
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(key=lambda x: x["cpu"], reverse=True)

    print("\nTop CPU Processes")
    print("-" * 60)

    for process in processes[:5]:
        print(
            f"PID: {process['pid']:<7} "
            f"CPU: {process['cpu']:>5.1f}%  "
            f"RAM: {process['memory']:>5.1f}%  "
            f"{process['name']}"
        )


def generate_alerts(cpu, ram, disk):
    alerts = []

    if cpu >= CPU_LIMIT:
        alerts.append(f"High CPU usage detected: {cpu}%")

    if ram >= RAM_LIMIT:
        alerts.append(f"High RAM usage detected: {ram}%")

    if disk >= DISK_LIMIT:
        alerts.append(f"High Disk usage detected: {disk:.2f}%")

    print("\nAlerts")
    print("-" * 60)

    if alerts:
        for alert in alerts:
            print(f"[WARNING] {alert}")
    else:
        print("[OK] System is healthy.")


# ==============================
# Main Program
# ==============================

def main():

    print_header()

    cpu = check_cpu()
    ram = check_memory()
    disk = check_disk()

    check_uptime()
    check_processes()

    generate_alerts(cpu, ram, disk)

    print("\n" + "=" * 60)
    print("Monitoring completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()