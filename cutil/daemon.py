from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import profiler
import argparse
#Creates and parses command line arguments.
parser = argparse.ArgumentParser()

parser.add_argument('-o',"--profile")

args = parser.parse_args()

if args.profile == "":
   print("No profile specified. Please specify a profile.")
   exit(1) 

profile = profiler.load(args.profile)

print(profile)

#OOP in python. Humanity is evolving lol.
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File {event.src_path} has been modified.")            

#if __name__ == "__main__":
#    path = 
#    event_handler = FileChangeHandler()
#    Observer = Observer()
    
