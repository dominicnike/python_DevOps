import psutil
import time
import logging
import argparse
from datetime import datetime

# Set up logging
log_file = "system_monitor.log"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - CPU Usage: %(message)s%%, Memory Usage: %(message)s%%', handlers=[logging.FileHandler(log_file), logging.StreamHandler()])
logger = logging.getLogger()

def log_system_usage(interval, duration):
    start_time = time.time()
    while True:
        # Get CPU and memory usage
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent

        # Log the usage
        logger.info(f"{cpu_usage}, {memory_usage}")

        # Check if the duration has been reached
        if duration and (time.time() - start_time) >= duration:
            break

        # Sleep for the specified interval
        time.sleep(interval - 1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Monitor system CPU and memory usage.')
    parser.add_argument('--interval', type=int, default=10, help='Logging interval in seconds (default: 10)')
    parser.add_argument('--duration', type=int, default=0, help='Monitoring duration in seconds (default: 0, which means run indefinitely)')
    args = parser.parse_args()

    log_system_usage(args.interval, args.duration)
