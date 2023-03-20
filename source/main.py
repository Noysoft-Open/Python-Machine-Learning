import numpy

class Main:

    def __init__(self):
        self.speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    def meanvalue(self):
        return numpy.mean(self.speed)
