import gpio
import threading
import datetime
import time


def time_between_times(time, early, late):
    if early <= time < late:
        return True
    elif late < early:
        return not time_between_times(time, late, early)
    else:
        return False

def time_between_times_test():
    # Minutes work
    assert time_between_times((0, 0, 1), (0, 0, 0), (0, 0, 2))
    assert not time_between_times((0, 0, 0), (0, 0, 1), (0, 0, 2))

    # Hours work
    assert time_between_times((0, 1, 0), (0, 0, 0), (0, 2, 0))
    assert not time_between_times((0, 0, 0), (0, 1, 0), (0, 2, 0))

    # Days work
    assert time_between_times((1, 0, 0), (0, 0, 0), (2, 0, 0))
    assert not time_between_times((0, 0, 0), (1, 0, 0), (2, 0, 0))

    # Normal wrapping works
    assert time_between_times((0, 0, 59), (0, 0, 58), (0, 1, 0))
    assert time_between_times((0, 23, 0), (0, 22, 0), (1, 0, 0))

    # Day wrapping works
    assert time_between_times((6, 0, 0), (5, 0, 0), (0, 0, 0))
    assert time_between_times((0, 0, 0), (6, 0, 0), (1, 0, 0))
    assert not time_between_times((1, 0, 0), (6, 0, 0), (0, 0, 0))

    # Inclusivity works
    assert time_between_times((0, 0, 0), (0, 0, 0), (0, 0, 1))
    assert not time_between_times((0, 0, 1), (0, 0, 0), (0, 0, 1))


DEFAULT_SCHEDULE = [
    ((0, 7, 0), 21),
    ((0, 11, 0), 17),
    ((0, 18, 0), 21),
    ((0, 23, 0), 17),

    ((1, 7, 0), 21),
    ((1, 11, 0), 17),
    ((1, 18, 0), 21),
    ((1, 23, 0), 17),

    ((2, 7, 0), 21),
    ((2, 11, 0), 17),
    ((2, 18, 0), 21),
    ((2, 23, 0), 17),

    ((3, 7, 0), 21),
    ((3, 11, 0), 17),
    ((3, 18, 0), 21),
    ((3, 23, 0), 17),

    ((4, 7, 0), 21),
    ((4, 11, 0), 17),
    ((4, 18, 0), 21),
    ((4, 23, 0), 17),

    ((5, 7, 0), 23),
    ((5, 23, 0), 17),

    ((6, 7, 0), 21),
    ((6, 23, 0), 17),
]

class Schedule(object):
    def __init__(self):
        self.heat_on = False
        gpio.heat_off()

        self.schedule = DEFAULT_SCHEDULE

    def desired_temp(self, time):
        for i in range(len(self.schedule)):
            start = self.schedule[i][0]
            end = self.schedule[(i + 1) % len(self.schedule)][0]

            if time_between_times(time, start, end):
                return self.schedule[i][1]

    def run(self):
        now = datetime.datetime.now()
        time = (now.weekday(), now.hour, now.minute)

        temp = gpio.get_temp()
        desired_temp = self.desired_temp(time)

        if self.heat_on and temp > (desired_temp + 0.5):
            gpio.heat_off()
            self.heat_on = False
        elif not self.heat_on and temp < desired_temp:
            gpio.heat_on()
            self.heat_on = True


def monitor_func(stop_event, scheduler):
    scheduler.run()

    while not stop_event.wait(30):
        scheduler.run()

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
    return scheduler.heat_on
