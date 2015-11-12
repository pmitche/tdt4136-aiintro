__author__ = 'Paul'

class Schedule(object):

    DECREMENT = 0.1
    TEMP = 0

    def __init__(self, temperature):
        self.temperature = temperature

    def schedule(self):
        self.temperature -= self.DECREMENT
        self.TEMP = self.temperature
        return self.temperature