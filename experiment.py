import numpy
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


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

    def plot_x(self, start):
        plt.plot(self.__x[start:-1])
        plt.show()
