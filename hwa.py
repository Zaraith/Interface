from tkinter import Tk, Menu, Button, LabelFrame, Entry, Label
from tkinter.filedialog import askopenfilename, sys
from tkinter.messagebox import askyesno, showerror

import experiment
import numbers


class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.__experiment = experiment.Experiment()
        self.__create_menu()
        self.__create_widgets()

    def __create_menu(self):
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Open', command=self.__do_fileopen)
        filemenu.add_command(label='Quit', command=self.__do_filequit)
        menubar.add_cascade(label='File', menu=filemenu)
        self.config(menu=menubar)

    def __create_widgets(self):
        label_frame = LabelFrame(self, text='X Curve', padx=30, pady=30)
        label_frame.place(x=15, y=15)
        label = Label(label_frame, text='Enter a number to truncate beginning of signal')
        label.grid(column=0, row=0)
        self.__truncate_edit = Entry(label_frame, background='white')
        self.__truncate_edit.insert(0, '0')
        self.__truncate_edit.bind()
        self.__truncate_edit.grid(column=0, row=1)
        plot_time_button = Button(label_frame, text='Plot Time Domain', command=self.__plot_time)
        plot_time_button.grid(column=0, row=3)
        plot_frequency_button = Button(label_frame, text='Plot Frequency Domain')
        plot_frequency_button.grid(column=0, row=4)

    def __do_filequit(self):
        if askyesno('Quit', 'Are you sure to quit ?'):
            sys.exit()

    def __do_fileopen(self):
        filename = askopenfilename(title='Select File',
                                   filetypes=[('Text files', '.txt')])
        self.__experiment.load_data(filename)

    def __plot_time(self):
        start_string = self.__truncate_edit.get()
        start = MainWindow.__validate_positive_number(start_string)
        if isinstance(start, numbers.Integral):
            self.__experiment.plot_x(start)
        else:
            showerror('Error', 'Enter a correct number to truncate')

    @staticmethod
    def __validate_positive_number(s):
        try:
            start = int(s)
        except ValueError as e:
            return False
        if start < 0:
            return False
        return start


if __name__ == '__main__':
    app = MainWindow()
    app.title('Noise Analysis')
    app.geometry('800x400+350+150')
    app.mainloop()
