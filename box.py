import tkinter
from tkinter import Tk, Button, LabelFrame, Checkbutton


self.l = LabelFrame(self, text="X Curve", padx=30, pady=30)
self.l.place(x=15,y=15)

Plot1 = Checkbutton(self.l, text="Plot Frequency Domain")
Plot1.grid(column=0, row=0)

Plot2 = Checkbutton(self.l, text="Plot Time Domain")
Plot2.grid(column=0, row=1)


self = Tk()
self.geometry("500x500+500+300")
self['bg']='white'
self.title('Noise')
self.mainloop()