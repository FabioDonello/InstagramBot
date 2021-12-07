import time
import threading

def progress_control():
    for val in range(100):
        print("sono nel thread")
        if ev.is_set():
            print("esco")
            break
        time.sleep(1)