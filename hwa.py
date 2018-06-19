from tkinter import Tk, Menu
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno
import experiment

import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.__experiment = experiment.Experiment()
        self.menubar = Menu(self)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Open', command=self.__do_fileopen)
        self.filemenu.add_command(label='Quit', command=self.__do_filequit)
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.config(menu=self.menubar)

    def __do_filequit(self):
        if askyesno('Quit', 'Are you sure to quit ?'):
            self.quit()

    def __do_fileopen(self):
        filename = askopenfilename(title='Select File',
                                   filetypes=[('Text files', '.txt')])
        self.__experiment.load_data(filename)
        plt.plot(self.__experiment.x()[2:-1])
        plt.show()


if __name__ == '__main__':
    app = MainWindow()
    app.title('Human Walk Analysis')
    app.geometry('500x400+350+400')
    app.mainloop()
