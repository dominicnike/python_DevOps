import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import getpass

# Set up logging
log_file = "Task 1/monitor.log"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[logging.FileHandler(log_file), logging.StreamHandler()])
logger = logging.getLogger()

class Watcher:
    def __init__(self, directory_to_watch):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Log file creation
            logger.info(f"Created file: {event.src_path} by user: {getpass.getuser()}")

        elif event.event_type == 'modified':
            # Log file modification
            logger.info(f"Modified file: {event.src_path} by user: {getpass.getuser()}")

        elif event.event_type == 'deleted':
            # Log file deletion
            logger.info(f"Deleted file: {event.src_path} by user: {getpass.getuser()}")

if __name__ == '__main__':
    path = "C:/Users/tobi-duru/Documents/python_projects/py_project/Task 1"  
    w = Watcher(path)
    w.run()
