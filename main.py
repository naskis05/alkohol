from tkinter import *
from tkinter.font import BOLD, Font
from tkinter.ttk import *
x=0
logs=Tk()
logs.title('Alkohola tests')
logs.geometry('640x480')
a=Canvas(logs, width=640, height=480, bg='gray')
a.place(x=0, y=0)
#Sākuma ekrāns
label = Label(logs, text="Tests par alkoholu",font=25)
label.place(x=250, y=100, height=20, width=150)

a1=IntVar()


def pirmaisuzd():
  J1=Label(logs, text='Cik daudz ir 1 promile?', font=15)
  R1=Checkbutton(logs, text='0,5%', variable = a1, onvalue=2, offvalue=0)
  R2=Checkbutton(logs, text='1%', variable = a1, onvalue=3, offvalue=0)
  R3=Checkbutton(logs, text='0,1%', variable = a1, onvalue=1, offvalue=0)
  J1.place(x=250, y=100)
  R1.place(x=250, y=150)
  R2.place(x=250, y=200)
  R3.place(x=250, y=250)

def navsākumaekrāns():
  label.place_forget()
  Sākt.place_forget()
  pirmaisuzd()
  
Sākt = Button(logs, text='Sākt testu', command=navsākumaekrāns)
Sākt.place(x=300, y=300)

  




logs.mainloop()





