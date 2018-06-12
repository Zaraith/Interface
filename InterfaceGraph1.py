""" Importation des modules utilisés """
import tkinter

""" Création d'une classe pour y mettre l'appli"""

class interfacegraph_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        """ Afin de référencer le parent """
        self.parent = parent
        """ Afin de séparer le code des éléments créer et la logique du programme """
        self.initialize()

    def initialize(self):
        self.grid()
        """ grid afin de positionner les widgets comme voulu """

""" Création du "Main" le premier élément de l'interface/l'application """
if __name__ == "__main__":
    app = interfacegraph_tk(None)
    app.title('Human Walk Analysis')
    app.geometry("500x400+350+400")

    app.mainloop()




