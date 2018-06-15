import csv


class Experiment:

    def load_data(self, filename):
        with open(filename, 'r') as file:
            print(file.read())

    def file_from_txt_to_table():
    	with open('C:/Users/anzou/Documents/CoursM1/Python/Git/staticnoise 29052018_001_2018_5_29 Marker30.txt', newline='') as csvfile:
    		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    		for row in spamreader:
    			print(', '.join(row))

