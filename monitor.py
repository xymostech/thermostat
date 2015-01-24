import gpio
import threading
import datetime
import time


schedule = [
    # 12-1 1-2    2-3    3-4
    False, False, False, False,
    # 4-5  5-6    6-7    7-8
    False, False, False, True,
    # 8-9 9-10  10-11  11-12
    True, True, False, False,
    # 12-1 1-2    2-3    3-4
    False, False, False, False,
    # 4-5  5-6    6-7    7-8
    False, False, True, True,
    # 8-9 9-10  10-11 11-12
    True, True, True, False,
]

TEMP_THRESHOLD_LOW = 21.0
TEMP_THRESHOLD_HIGH = 21.5

class Schedule(object):
    def __init__(self):
        self.heat_on = False
        gpio.heat_off()

    def run(self):
        now = datetime.datetime.now()
        hour = now.hour

        temp = gpio.get_temp()

        if self.heat_on and (not schedule[hour] or temp > TEMP_THRESHOLD_HIGH):
            gpio.heat_off()
            self.heat_on = False
        elif not self.heat_on and schedule[hour] and temp < TEMP_THRESHOLD_LOW:
            gpio.heat_on()
            self.heat_on = True


def monitor_func(stop_event, scheduler):
    while not stop_event.is_set():
        scheduler.run()

        time.sleep(30)

monitor_thread = None
stop_event = threading.Event()
scheduler = Schedule()

def start_monitoring():
    global monitor_thread
    if not monitor_thread:
        stop_event.clear()
        monitor_thread = threading.Thread(
            target=monitor_func,
            args=(stop_event, scheduler)
        )
        monitor_thread.start()

def stop_monitoring():
    if monitor_thread:
        stop_event.set()
        monitor_thread.join()

def heat_on():
    return heat_event.is_set()
