from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File {event.src_path} has been modified.")            
