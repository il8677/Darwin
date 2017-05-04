import numpy

def sig(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + numpy.exp(-x))

class finch:
    def __init__(self):
        self.wl0 = 2*numpy.random.random((3,1)) - 1
        self.wl1 = 2*numpy.random.random((3,1)) - 1

    def sig(x, deriv=False):
        if (deriv == True):
            return x * (1 - x)
        return 1 / (1 + numpy.exp(-x))
    def go(self, hunger, currentTree,currentFood):
        numpy.random.seed(1)

        l0 = numpy.array([hunger,currentTree,currentFood])

        l1 = self.sig(numpy.dot(l0,self.wl0))

        o = self.sig(numpy.dot(l1,self.wl1))

        return o