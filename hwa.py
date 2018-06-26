from tkinter import Tk, Menu, Button, Entry, Label, DISABLED, ACTIVE, LabelFrame, Y, X
from tkinter.filedialog import askopenfilename, sys
from tkinter.messagebox import askyesno, showerror

import experiment


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
        file_label_frame = LabelFrame(self, text='File Name')
        file_label_frame.pack()
        self.__filename_label = Label(file_label_frame, text='<no file>')
        self.__filename_label.pack()
        x_label_frame = LabelFrame(self, text='X Curve')
        x_label_frame.pack(expand=False, fill=Y, pady=60)
        truncate_label = Label(x_label_frame, text='Enter a number to truncate beginning of signal')
        truncate_label.pack(expand=True, fill=X)
        self.__truncate_edit = Entry(x_label_frame, background='white')
        self.__truncate_edit.insert(0, '0')
        self.__truncate_edit.bind()
        self.__truncate_edit.pack(expand=True, fill=X)
        self.__plot_time_button = Button(x_label_frame, text='Plot Time Domain', state=DISABLED, command=self.__plot_time_domain)
        self.__plot_time_button.pack(expand=True, fill=X)
        self.__plot_frequency_button = Button(x_label_frame, text='Plot Frequency Domain', state=DISABLED, command=self.__plot_frequency_domain)
        self.__plot_frequency_button.pack(expand=True, fill=X)

    def __do_filequit(self):
        if askyesno('Quit', 'Are you sure to quit ?'):
            sys.exit()

    def __do_fileopen(self):
        filename = askopenfilename(title='Select File',
                                   filetypes=[('Text files', '.txt')])
        self.__experiment.load_data(filename)
        self.__filename_label.config(text=filename)
        self.__plot_time_button.config(state=ACTIVE)
        self.__plot_frequency_button.config(state=ACTIVE)

    def __plot_time_domain(self):
        start_string = self.__truncate_edit.get()
        if MainWindow.__validate_positive_number(start_string):
            self.__experiment.plot_x(int(start_string))
        else:
            showerror('Error', 'Enter a correct number to truncate')

    def __plot_frequency_domain(self):
        self.__experiment.plot_x_f()

    @staticmethod
    def __validate_positive_number(s):
        try:
            start = int(s)
        except ValueError as e:
            return False
        if start < 0:
            return False
        return True


if __name__ == '__main__':
    app = MainWindow()
    app.title('Noise Analysis')
    app.geometry('800x400+350+150')
    app.mainloop()
