class Time(object):

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.set_hours(hours)
        self.set_minutes(minutes)
        self.set_seconds(seconds)

    def set_hours(self, hours):
        self._hours = hours % 24

    def set_minutes(self, minutes):
        self._minutes = minutes

    def set_seconds(self, seconds):
        self._seconds = seconds

    def get_hours(self):
        return self._hours

    def get_minutes(self):
        return self._minutes

    def get_seconds(self):
        return self._seconds

    def get_elapsed_time(self):
        return self.get_hours() * 3600 + self.get_minutes() * 60 + self.get_seconds()

    def set_elapsed_time(self, seconds):
        hours = seconds / 3600
        self.set_hours(hours)
        seconds -= hours * 3600
        minutes = seconds / 60
        self.set_minutes(minutes)
        seconds -= minutes * 60
        self.set_seconds(seconds)

    def __str__(self):
        return "Time: %d:%d:%d" % (self.get_hours(), self.get_minutes(), self.get_seconds())

    hours = property(get_hours, set_hours)
    minutes = property(get_minutes, set_minutes)
    seconds = property(get_seconds, set_seconds)
    elapsed_time = property(get_elapsed_time, set_elapsed_time)

t = Time(10, 19, 10)
print t.elapsed_time
t.elapsed_time = 555550
print t.elapsed_time
print t
