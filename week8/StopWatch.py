import time


class StopWatch(object):

    def __init__(self, start_time=time.time(), end_time=-1):
        self.set_start_time(start_time)
        self.set_end_time(end_time)

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def set_start_time(self, start_time):
        self._start_time = start_time

    def set_end_time(self, end_time):
        self._end_time = end_time

    def start(self):
        self.set_start_time(time.time())
        self.set_end_time(-1)

    def stop(self):
        self.set_end_time(time.time())

    def elapsed_time(self):
        if self.get_end_time() == -1:
            return None
        return round((self.get_end_time() - self.get_start_time())*1000)

    start_time = property(get_start_time, set_start_time)
    end_time = property(get_end_time, set_end_time)

sw = StopWatch()
time.sleep(0.1)
sw.stop()
print sw.elapsed_time()
sw.start()
time.sleep(0.2)
print sw.elapsed_time()
sw.stop()
print sw.elapsed_time()