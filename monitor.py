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
    True, True, True, True,
]


class Schedule:
    def __init__(self, heat_event):
        self.heat_on = False
        self.heat_event = heat_event

        self.heat_event.clear()

        gpio.heat_off()

    def run(self):
        now = datetime.datetime.now()

        hour = now.hour

        if not self.heat_on and schedule[hour]:
            gpio.heat_on()
            self.heat_on = True
            self.heat_event.set()
        elif self.heat_on and not schedule[hour]:
            gpio.heat_off()
            self.heat_on = False
            self.heat_event.clear()


def monitor_func(stop_event, heat_event):
    schedule = Schedule(heat_event)
    schedule.run()

    while not stop_event.is_set():
        schedule.run()

        time.sleep(30)

monitor_thread = None
stop_event = threading.Event()
heat_event = threading.Event()

def start_monitoring():
    global monitor_thread
    if not monitor_thread:
        stop_event.clear()
        monitor_thread = threading.Thread(
            target=monitor_func,
            args=(stop_event, heat_event)
        )
        monitor_thread.start()

def stop_monitoring():
    if monitor_thread:
        stop_event.set()
        monitor_thread.join()

def heat_on():
    return heat_event.is_set()
