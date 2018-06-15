import csv
import numpy

class Experiment:

    def load_data(self, filename):
    	self.__x, self.__y, self.__z = numpy.loadtxt("C:/Users/anzou/Documents/CoursM1/Python/Git/staticnoise 29052018_001_2018_5_29 Marker30.txt", unpack=True)

    def x(self):
    	return self.__x

    def y(self):
    	return self.__y

    def z(self):
    	return self.__z
