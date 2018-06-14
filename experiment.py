class Experiment:

    def load_data(self, filename):
        with open(filename, 'r') as file:
            print(file.read())
