import gpio
import threading
import datetime
import time
import db
import schedule


class TempMonitor(object):
    def __init__(self):
        self.heat_on = False
        gpio.heat_off()

    def run(self):
        now = datetime.datetime.now()
        curr_schedule = schedule.schedule_from_db()
        temp = gpio.get_temp()

        desired_temp = curr_schedule.desired_temp_at_time(now)

        if self.heat_on and temp > (desired_temp + 0.5):
            gpio.heat_off()
            self.heat_on = False
        elif not self.heat_on and temp < desired_temp:
            gpio.heat_on()
            self.heat_on = True

        with db.get_db() as cursor:
            cursor.execute(
                "INSERT INTO temp_data VALUES (NULL, strftime('%s', 'now'), ?)",
                (temp,))

            cursor.execute("""
                INSERT INTO heat_active_data VALUES
                (NULL, strftime('%s', 'now'), ?)""",
                (self.heat_on,))


def monitor_func(stop_event, monitor):
    monitor.run()

    while not stop_event.wait(30):
        monitor.run()

monitor_thread = None
stop_event = threading.Event()
monitor = TempMonitor()

def start_monitoring():
    global monitor_thread
    if not monitor_thread:
        stop_event.clear()
        monitor_thread = threading.Thread(
            target=monitor_func,
            args=(stop_event, monitor)
        )
        monitor_thread.start()

def stop_monitoring():
    if monitor_thread:
        stop_event.set()
        monitor_thread.join()

def heat_on():
    return monitor.heat_on
