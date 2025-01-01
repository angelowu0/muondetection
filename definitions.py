class MuonEvent(object):
    def __init__(self, time: int, decay_time: int):
        # UNIX time
        self.time = time
        # milliseconds
        self.decay_time = decay_time

    def __str__(self):
        return f"Time: {self.time}, Decay Time: {self.decay_time}"

    def get_time(self):
        return self.time

    def get_decay_time(self):
        return self.decay_time
