import tkinter

""" The Application will be put in a class """
class Interfacegraphique_tk(tkinter.Tk):


    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        """ Will serve as a reference to the parent """
        self.parent = parent
        """ To create a separation between the logical program and widgets/elements creation """
        self.initialize()
    def initialize(self):
        self.grid()


""" "Main" will be the first element of the application """
if __name__ == "__main__":
    app = Interfacegraphique_tk(None)
    app.title('Human Walk Analysis')
    app.geometry("500x400+350+400")
    app.mainloop()