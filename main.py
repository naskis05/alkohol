from tkinter import *
from tkinter.font import BOLD, Font
logs=Tk()
logs.title('Alkohola tests')
logs.geometry('640x480')
a=Canvas(logs, width=640, height=480, bg='yellow')
a.place(x=0, y=0)
#Sākuma ekrāns
label = Label(logs, text="Tests par alkoholu", height=2, width=15, font=25)
label.place(x=250, y=100)


def navsākumaekrāns():
  label.place_forget()
  Sākt.place_forget()

Sākt = Button(logs, text='Sākt testu', command=navsākumaekrāns)
Sākt.place(x=300, y=300)

logs.mainloop()





