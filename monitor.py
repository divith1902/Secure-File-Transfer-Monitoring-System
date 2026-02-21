from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import logging
import os
from hash_utils import calculate_hash
from config import SENSITIVE_DIRECTORIES
import psutil

logging.basicConfig(
    filename="audit_log.txt",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

file_transfer_counter = 0

def get_usb_drives():
    usb_list = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if 'removable' in partition.opts:
            usb_list.append(partition.device)
    return usb_list


class MonitorHandler(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            self.process_event("CREATED", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            logging.warning(f"File Deleted: {event.src_path}")
            print(f"⚠️ File Deleted: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            self.process_event("MODIFIED", event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            self.process_event("MOVED", event.src_path, event.dest_path)

    def process_event(self, event_type, src, dest=None):
        global file_transfer_counter
        file_transfer_counter += 1

        file_hash = calculate_hash(src)

        # Bulk transfer detection
        if file_transfer_counter > 20:
            print("⚠️ Bulk File Transfer Detected")
            logging.warning("Bulk File Transfer Detected")

        # Sensitive directory check
        for sensitive_dir in SENSITIVE_DIRECTORIES:
            if src.startswith(sensitive_dir):
                print("🔐 Sensitive File Event Detected")

                # USB detection
                usb_drives = get_usb_drives()
                if dest:
                    for usb in usb_drives:
                        if dest.startswith(usb):
                            alert = f"ALERT: Sensitive file moved to USB -> {dest}"
                            print(alert)
                            logging.warning(alert)

        log_message = f"{event_type} | {src} | HASH: {file_hash}"
        logging.info(log_message)
        print(log_message)


observer = Observer()
observer.schedule(MonitorHandler(), path="C:\\", recursive=True)
observer.start()

print("🚀 Monitoring Started (Project 2 Advanced Version)...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()