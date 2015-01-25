import db


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

class Schedule(object):
    def __init__(self, schedule):
        self.schedule = schedule

    def desired_temp_at_time(self, time):
        time_data = (time.weekday(), time.hour, time.minute)

        for i in range(len(self.schedule)):
            start = self.schedule[i][0]
            end = self.schedule[(i + 1) % len(self.schedule)][0]

            if time_between_times(time_data, start, end):
                return self.schedule[i][1]

def schedule_from_db():
    schedule = []
    with db.get_db() as cursor:
        for row in cursor.execute("SELECT * FROM schedule"):
            schedule.append((
                (row['weekday'], row['hour'], row['minute']),
                row['desired_temp']
            ))

    schedule.sort(key=lambda s: s[0])

    return Schedule(schedule)
