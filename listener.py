import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from environment import *
from handler import handler


def on_created(event):
    handler()

if __name__ == "__main__":

    event_hander = FileSystemEventHandler()
    event_hander.on_created = on_created
    path = path_osx()
    observer = Observer()
    observer.schedule(event_hander, path, recursive=True)
    observer.start()
    try:
        print("Monitoring...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print(" Done monitoring!")
    observer.join()
