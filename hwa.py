import tkinter


class MainWindow(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)


if __name__ == '__main__':
    app = MainWindow()
    app.title('Human Walk Analysis')
    app.geometry('500x400+350+400')
    app.mainloop()
