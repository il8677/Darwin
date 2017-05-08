import numpy


def sig(x, deriv=False):
    if deriv == True:
        return x * (1 - x)
    return 1 / (1 + numpy.exp(-x))


class Finch:

    def __init__(self):
        self.wl0 = 2*numpy.random.random((3, 4)) - 1
        self.wl1 = 2*numpy.random.random((4,3)) - 1

    def sig(self,x, deriv=False):
        if (deriv == True):
            return x * (1 - x)
        return 1 / (1 + numpy.exp(-x))

    def go(self, hunger, currentTree,currentFood):
        numpy.random.seed(1)

        self.l0 = numpy.array([hunger,currentTree,currentFood])

        self.l1 = numpy.empty(shape=(4,1))

        for i in range(0,4):
            self.l1[i]=sig(numpy.dot(self.l0,self.wl0))
        o = numpy.empty(shape=(3,1))
        for i in range(0,3):
            o[i] = sig(numpy.dot(self.l1,self.wl1))

        return o