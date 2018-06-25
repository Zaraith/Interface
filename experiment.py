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
        x = self.__x[start:-1]
        plt.plot(x)
        plt.show()

    def plot_x_f(self):
        x_f = numpy.fft.fft(self.__x - numpy.mean(self.__x))
        half = int(len(x_f) / 2)
        plt.plot(numpy.abs(x_f[1:half]))
        # plt.plot(numpy.abs(x_f))

        plt.subplot(2, 2, 1)
        plt.plot(numpy.abs(x_f[1:half]))
        plt.title('Amplitude')
        plt.grid(True)

        plt.subplot(2, 2, 2)
        plt.plot(numpy.abs(x_f[1:half]))
        plt.title('Phase')
        plt.grid(True)

        plt.subplot(2, 2, 3)
        plt.plot(numpy.abs(x_f[1:half]))
        plt.title('Real')
        plt.grid(True)

        plt.subplot(2, 2, 4)
        plt.plot(numpy.abs(x_f[1:half]))
        plt.title('Imaginary')
        plt.grid(True)

        plt.show()
