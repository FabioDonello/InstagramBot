import schedule
import threading
import time


def job():
    print("I'm running on thread %s" % threading.current_thread())
    return schedule.CancelJob


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every().day.at('17:02').do(run_threaded, job)
schedule.every().day.at('17:01:58').do(run_threaded, job)
'''schedule.every(2).seconds.do(run_threaded, job)
schedule.every(4).seconds.do(run_threaded, job)
schedule.every(20).seconds.do(run_threaded, job)
schedule.every(60).seconds.do(run_threaded, job)
'''
while True:
    schedule.run_pending()
    time.sleep(1)
