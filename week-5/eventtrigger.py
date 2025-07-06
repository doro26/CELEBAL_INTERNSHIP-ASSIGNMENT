import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "C:/Users/ananya/Downloads"
SCRIPT_TO_RUN = "C:/Users/ananya/OneDrive/Desktop/ananya/exportfiles.py"

class CSVHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".csv"):
            print(f"New CSV detected: {event.src_path}")
            os.system(f'python "{SCRIPT_TO_RUN}"')

if __name__ == '__main__':
    event_handler = CSVHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()
    print(f"Watching folder: {WATCH_FOLDER}")
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
        print("Observer stopped.")
    observer.join()
