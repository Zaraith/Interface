import numpy


class Experiment:

    def __init__(self):
        self.__x = numpy.empty(0)
        self.__y = numpy.empty(0)
        self.__z = numpy.empty(0)

    def load_data(self, filename):
        self.__x, self.__y, self.__z = numpy.loadtxt(filename, unpack=True)

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def z(self):
        return self.__z
