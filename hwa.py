from tkinter import Tk, Menu
from tkinter.messagebox import *
from tkinter.filedialog import *


class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.menubar = Menu(self)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Open', command=self.__open_file)
        self.filemenu.add_command(label='Quit', command=self.__do_filequit)
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.config(menu=self.menubar)

    def __do_filequit(self):
        if askyesno('Quit', 'Are you sure to quit ?'):
            showwarning('Warning', 'Bye !')
            self.quit()
    def __open_file(self):
        filename = askopenfile(title='Choose a file', filetypes=[('TEXT files', '.txt')])


if __name__ == '__main__':
    app = MainWindow()
    app.title('Human Walk Analysis')
    app.geometry('500x400+350+400')
    app.mainloop()
