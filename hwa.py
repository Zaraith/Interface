import tkinter


class MainWindow(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)
        self.menubar = tkinter.Menu(self)
        self.menu = tkinter.Menu(self.menubar, tearoff=0)
        self.menu.add_command(label="Quit")
        self.menubar.add_cascade(label="File", menu=self.menu)
        self.config(menu=self.menubar)


if __name__ == '__main__':
    app = MainWindow()
    app.title('Human Walk Analysis')
    app.geometry('500x400+350+400')
    app.mainloop()
