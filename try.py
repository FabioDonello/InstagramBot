from try2 import *
import multiprocessing
import time

t = multiprocessing.Process(target=progress_control)
t.start()
print("aspetto 10 secondi")
time.sleep(10)
t.terminate()







